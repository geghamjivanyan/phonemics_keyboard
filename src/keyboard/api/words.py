#
import json
from typing import List, Optional, Dict, Any

#
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.db.models.functions import Right
from django.core.exceptions import ValidationError
from django.db import transaction

from ..models.words import Word
from ..models.koran import Koran
from ..models.translit_words import TranslitWord
from ..models.rhythms import Rhythm
from ..models.hamza_words import HamzaWord

from ..tools.utils import is_vowel, sort_by_frequency, is_keyboard_changed
from ..tools.utils import change_hamza, change_text
from ..tools.constants import Diacritics as D
from ..tools.transformation_tools import from_arabic_to_translit, from_translit_to_arabic 
from ..tools.transformation_tools import classify, split, apply_transformation_rules

from .hamza_words import HamzaWordView

class WordView(View):
    """View for handling word-related operations."""

    def get(self, request) -> HttpResponse:
        """
        Get words from Koran blocks.
        
        Args:
            request: HTTP request object containing count parameter
            
        Returns:
            HttpResponse with status 200 if successful
        """
        try:
            count = int(request.GET.get("count", 0))
            blocks = Koran.objects.filter(
                id__gt=count*600,
                id__lt=(count+1)*600-1
            )
            
            with transaction.atomic():
                for block in blocks:
                    self._process_koran_block(block)
                    
            return HttpResponse(
                status=200,
                content_type="application/json; charset=utf-8",
            )
        except (ValueError, ValidationError) as e:
            return JsonResponse(
                {"error": str(e)},
                status=400
            )
        except Exception as e:
            return JsonResponse(
                {"error": "Internal server error"},
                status=500
            )

    def _process_koran_block(self, block: Koran) -> None:
        """Process a single Koran block and create/update Word objects."""
        words = block.arabic.split(' ')
        shrifts = block.easy_shrift.split(' ')

        if len(words) == 2:
            self._create_or_update_word(words[0], words[1], shrifts[0], shrifts[1])
        elif len(words) == 1:
            self._create_or_update_word(words[0], None, shrifts[0], None)
        else:
            # Process first word
            self._create_or_update_word(words[0], words[1], shrifts[0], shrifts[1])
            
            # Process middle words
            for i in range(1, len(words)-1):
                self._create_or_update_word(
                    words[i],
                    words[i+1],
                    shrifts[i],
                    shrifts[i+1]
                )
            
            # Process last word
            self._create_or_update_word(
                words[-1],
                None,
                shrifts[-1],
                None
            )

    def _create_or_update_word(
        self,
        current: str,
        next_word: Optional[str],
        es_current: str,
        es_next: Optional[str]
    ) -> None:
        """Create or update a Word object."""
        word, _ = Word.objects.get_or_create(
            current=current,
            next=next_word
        )
        word.es_current = es_current
        word.es_next = es_next
        word.save()

    @staticmethod
    def remove_dots(text: str) -> str:
        """
        Remove dots and diacritics from text.
        
        Args:
            text: Input text to process
            
        Returns:
            Processed text without dots and diacritics
        """
        text = text.encode('utf-8')
        
        for d in D.diacritics:
            text = text.replace(d, b'')
            
        for k, v in D.dotless.items():
            text = text.replace(k, v)
            
        return text.decode('utf-8')

    @staticmethod
    def remove(request) -> HttpResponse:
        """
        Remove all Word objects.
        
        Args:
            request: HTTP request object
            
        Returns:
            HttpResponse with status 200 if successful
        """
        try:
            with transaction.atomic():
                Word.objects.all().delete()
            
            return HttpResponse(
                status=200,
                content_type="application/json; charset=utf-8",
            )
        except Exception as e:
            return JsonResponse(
                {"error": "Failed to remove words"},
                status=500
            )
        
    @staticmethod
    def shadda(request) -> HttpResponse:
        """
        Apply shadda rules.
        
        Args:
            request: HTTP request object
            
        Returns:
            HttpResponse with status 200 if successful
        """
        #(064e, 064f, 0650) + 0651
        rules = {
            chr(0x064e) + chr(0x0651): chr(0x0651) + chr(0x064e), 
            chr(0x064f) + chr(0x0651): chr(0x0651) + chr(0x064f),
            chr(0x0650) + chr(0x0651): chr(0x0651) + chr(0x0650),
        }    

        try:
            words = Word.objects.all()

            for word in words:
                for k in rules:
                    word.current.replace(k, rules[k])
                    if word.next:
                        word.next.replace(k, rules[k])
                word.save()

            
            return HttpResponse(
                status=200,
                content_type="application/json; charset=utf-8",
            )
        except Exception as e:
            print("Error", e)
            return JsonResponse(
                {"error": "Failed to update shadda rules"},
                status=500
            )

    @staticmethod
    def search(request) -> HttpResponse:
        """
        Search for word suggestions based on input text and rhythms.
        
        Args:
            request: HTTP request object containing text, rhythms, and keyboard parameters
            
        Returns:
            HttpResponse with suggestions data
        """
        try:
            body = json.loads(request.body)
            print("BDY", body)
            text = body.get('text', '')
            rhythms = body.get('rhythms', [])
            keyboard = body.get('keyboard', 0)
            is_changed = body.get('keyboardChanged', False)

            print("Search request - text:", text)
            print("Search request - rhythms:", rhythms)
            print("Search request - keyboard:", keyboard)
            print("Search request - is_changed:", is_changed)

            data = {
                "rhythms": rhythms,
                "suggestions": [],
                "text": text,
                "isHamza": False,
                "last_word": []
            }
            print("BODY", data)

            if is_changed:
                text = WordView._change_text(text, keyboard)
                data['text'] = text
                return JsonResponse({"data": data})
            
            # Handle hamza suggestions
            suggestions = WordView._manage_hamza(text, keyboard)
            print("Hamza suggestions:", suggestions)

            data['suggestions'] = suggestions

            if len(suggestions) == 1:
                text = change_text(text, suggestions[0])
                data['suggestions'] = []
                data['text'] = text
            elif len(suggestions) > 1:
                data['suggestions'] = suggestions
                data['isHamza'] = True    
            else:
                if text[-1] == " ":        
                    suggestions = WordView._suggest_next_word(text, rhythms)
                else:        
                    suggestions = WordView._suggest_next_syllable(text, rhythms)
                data['suggestions'] = suggestions
            data['rhythms'] = WordView._suggest_rhythms(text, rhythms)
            data['last_word'] = WordView.suggest_new_line(text)
            print("Final data:", data)
            return JsonResponse({"data": data})
            
        except json.JSONDecodeError as e:
            print("JSON Decode Error:", str(e))
            return JsonResponse(
                {"error": "Invalid JSON in request body"},
                status=400
            )
        except Exception as e:
            print("Unexpected error in search:", str(e))
            print("Error type:", type(e).__name__)
            import traceback
            print("Traceback:", traceback.format_exc())
            return JsonResponse(
                {"error": "Internal server error"},
                status=500
            )
    
    @staticmethod
    def _suggest_next_syllable(text: str, rhythms: Optional[List[str]]) -> List[str]:
        """
        Suggest next syllable based on input text and rhythms.
        
        Args:
            text: Input text
            rhythms: List of rhythm patterns
            
        Returns:
            List of suggested syllables
        """
        arabic = from_arabic_to_translit(text[1:])
        if not arabic:
            return []

        cut = split(arabic) if len(arabic) >= 3 else arabic
        syllables = cut.split(' ')
        data = []
        
        if len(syllables) > 1:
            rows = TranslitWord.objects.filter(
                prev__iexact=syllables[-2],
                current__iexact=syllables[-1]
            )
            data = [from_translit_to_arabic(row.next) for row in rows if row.next]
        else:
            rows = TranslitWord.objects.filter(prev__iexact=syllables[0])
            data = [from_translit_to_arabic(row.current) for row in rows if row.current]

        data = sort_by_frequency(data)
        print("DATA", data)
        pattern = classify(cut)
        print("TEXT", pattern)
        n = len(pattern)

        if type(rhythms) == str:
            rhythms = [rhythms]
        
        if rhythms is None:
            rhythms = [r['name'] for r in Rhythm.objects.values('name')]

        suggestions = []
        print("RRRRR", rhythms)
        for rhythm in rhythms:
            r = Rhythm.objects.get(name=rhythm)
            print("LEN", n, len(r.pattern))
            if n == len(2*r.pattern):
                continue
            print("RHYTHMS", r.pattern, (2*r.pattern)[n])
            next_pattern = (2*r.pattern)[n]
            
            for d in data:
                print("CLASS", classify(d))
                if classify(d) == next_pattern:
                    suggestions.append(d)

        return suggestions
    
    @staticmethod
    def _suggest_rhythms(text: str, rhythms: Optional[List[str]]) -> List[str]:
        """
        Suggest rhythms based on input text.
        
        Args:
            text: Input text
            rhythms: List of current rhythms
            
        Returns:
            List of suggested rhythms
        """
        print("=== _suggest_rhythms START ===")
        print("Input text:", text)
        print("Input rhythms:", rhythms)
        
        try:
            if not text:
                print("Empty text input")
                return []
                
            print("Text length:", len(text))
            print("First character:", text[0] if text else "empty")
            
            text = from_arabic_to_translit(text[1:])
            print("After transliteration:", text)
            
            parts = split(text)
            print("After split:", parts)
            
            pattern = classify(parts)
            print("Pattern:", pattern)
            
            if rhythms and rhythms[0].startswith(pattern):
                print("Using existing rhythms")
                return rhythms
            
            print("Querying database for rhythms")
            all_rhythms = Rhythm.objects.all()
            print("Found rhythms count:", all_rhythms.count())
            
            result = [
                r.name for r in all_rhythms
                if (2*r.pattern).startswith(pattern)
            ]
            print("Filtered rhythms:", result)
            print("=== _suggest_rhythms END ===")
            return result
            
        except Exception as e:
            print("=== _suggest_rhythms ERROR ===")
            print("Error type:", type(e).__name__)
            print("Error message:", str(e))
            import traceback
            print("Traceback:", traceback.format_exc())
            print("=== _suggest_rhythms ERROR END ===")
            return []


    @staticmethod
    def _suggest_next_word(text: str, rhythms: Optional[List[str]]) -> List[str]:
        """
        Suggest next word based on input text and rhythms.
        
        Args:
            text: Input text
            rhythms: List of rhythm patterns
            
        Returns:
            List of suggested words
        """
        if type(rhythms) == str:
            rhythms = [rhythms]
        if rhythms is None:
            rhythms = [r['name'] for r in Rhythm.objects.values('name')]

        current = text.strip().split(' ')[-1]
        cut = split(from_arabic_to_translit(text.strip().replace(' ', '')))
        pattern = classify(cut)
        suggestions = set()

        for rhythm in rhythms:
            r = Rhythm.objects.get(name=rhythm)
            if not (2*r.pattern).startswith(pattern):
                continue

            words = Word.objects.filter(current=current)
            for word in words:
                if not word.next:
                    continue

                n_cut = split(from_arabic_to_translit(word.next))
                n_pattern = classify(n_cut)

                if (2*r.pattern).startswith(pattern + n_pattern):
                    suggestions.add(word.next)

        return list(suggestions)

    @staticmethod
    def _suggest_next_word_1(text: str, rhythms: Optional[List[str]]) -> List[str]:
        """
        Suggest next word based on input text and rhythms.
        
        Args:
            text: Input text
            rhythms: List of rhythm patterns
            
        Returns:
            List of suggested words
        """
        if type(rhythms) == str:
            rhythms = [rhythms]
        if rhythms is None:
            rhythms = [r['name'] for r in Rhythm.objects.values('name')]

        text = text.strip().split(' ')[-1]
        S, M, L = WordView.get_S_M_L(text)
        cut = split(from_arabic_to_translit(text))
        pattern = classify(cut)
        suggestions = set()

        left = chr(0x064B) + ' ' + chr(0x0627)
        right = chr(0x0627) + chr(0x064B) + ' '

        for rhythm in rhythms:
            r = Rhythm.objects.get(name=rhythm)
            if not r.pattern.startswith(pattern):
                continue

            words = Word.objects.filter(current=text)
            for word in words:
                if not word.next:
                    continue
                    
                SW, MW, LW = WordView.get_S_M_L(word.next)
                ptr = classify(SW+MW)
                
                if not r.pattern.startswith(pattern+ptr):
                    continue
                    
                tr_word = from_arabic_to_translit(word.next)
                
                # Check various conditions for word suggestions
                if (not is_vowel(tr_word[0]) and
                    len(L) == 2 and
                    not is_vowel(L[0]) and
                    is_vowel(L[1])):
                    suggestions.add(word.next)
                elif (len(L) == 3 and
                      not is_vowel(L[0]) and
                      is_vowel(L[1]) and
                      is_vowel(L[2])):
                    suggestions.add(word.next)
                elif (len(L) == 3 and
                      not is_vowel(L[0]) and
                      is_vowel(L[1]) and
                      not is_vowel(L[2])):
                    if classify(split(L + SW)) == '12':
                        
                        suggestions.add(next + " ")

        return list(suggestions)

    @staticmethod
    def get_S_M_L(text: str) -> tuple[str, str, str]:
        """
        Split text into S (start), M (middle), and L (last) parts.
        
        Args:
            text: Input text
            
        Returns:
            Tuple of (S, M, L) parts
        """
        text = apply_transformation_rules(text)
        text = from_arabic_to_translit(text)
        
        # Find first CV index
        i = 0
        while i < len(text) - 1:
            if not is_vowel(text[i]) and is_vowel(text[i+1]):
                break
            i += 1
        
        S = text[:i]
        
        # Find last CV index
        j = len(text) - 1
        while j > 1:
            if is_vowel(text[j]) and not is_vowel(text[j-1]):
                j -= 1
                break
            j -= 1
        
        L = text[j:]
        M = text[i:j]
        
        return S, M, L

    @staticmethod
    def _manage_hamza(text: str, keyboard: int) -> List[str]:
        """
        Manage hamza suggestions based on input text and keyboard type.
        
        Args:
            text: Input text
            keyboard: Keyboard type (0 or 1)
            
        Returns:
            List of hamza suggestions
        """
        words = text.split(' ')
        word = change_hamza(words[-1])
        hmz = HamzaWord.objects.filter(hamza=word)
        
        data = []
        for h in hmz:
            if keyboard == 1:
                data.append(h.phonemic)
            else:
                data.append(h.easy_shrift)
        
        return list(set(data))

    
    @staticmethod
    def is_rhythmable(text):
        text = from_arabic_to_translit(text)

        if len(text) < 4:
            return False, 0 
        
        # vvcc
        if is_vowel(text[-4]) and is_vowel(text[-3]) and not is_vowel(text[-2]) and is_vowel(text[-1]):
            return True, 4
        
        # v(wy)cv
        if is_vowel(text[-4]) and not is_vowel(text[-2]) and is_vowel(text[-1]):
            if text[-3] in 'wy':
                return True, 4
            
        if len(text) > 6:
            # vvcvcvv
            if is_vowel(text[-7]) and is_vowel(text[-6]) and not is_vowel(text[-5]) and \
                is_vowel(text[-4]) and not is_vowel(text[-3]) and \
                is_vowel(text[-2]) and is_vowel(text[-1]):
                    return True, 7
            

        return False, 0
    
    @staticmethod
    def suggest_new_line(text):
        b, t = WordView.is_rhythmable(text)


        text = from_arabic_to_translit(text[1:])
        print("LW After transliteration:", text)
            
        parts = split(text)
        print("LW After split:", parts)
            
        pattern = classify(parts)
        print("LW Pattern:", pattern)
        suggestions = []
        
        if WordView.is_end_of_line(pattern):
            if b:
                suffix = text[-t:]

                rhymes = Word.objects.annotate(
                    ending=Right('next', t)
                ).filter(ending=suffix)
        
                suggestions = [w.next for w in rhymes]

        return suggestions
    

    @staticmethod
    def _change_text(text, keyboard):

        if keyboard == 2:
            text = HamzaWordView.remove_dots(text)
            return text

        words = text.strip().split(' ')
        for i in range(len(words)):
            words[i] = HamzaWord.objects.get(easy_shrift=words[i]).phonemic

        return ' ' + ' '.join(words)

    @staticmethod
    def is_end_of_line(pattern):
        n = len(pattern)
        if n % 2 == 0:
            if pattern[:n//2] == pattern[n//2:]:
                rhythms = Rhythm.objects.all()

                for rhythm in rhythms:
                    if rhythm.pattern == pattern[:n//2]:
                        return True 
        return False
    

    