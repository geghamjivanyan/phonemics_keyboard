#
import json

#
from django.views.generic import View
from django.http import HttpResponse
from django.db.models.functions import Right

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


class WordView(View):

    def get(self, request):
        count = int(request.GET.get("count", None))
        blocks = Koran.objects.filter(id__gt=count*600, id__lt=(count+1)*600-1)

        for block in blocks:
            words = block.arabic.split(' ')
            shrifts = block.easy_shrift.split(' ')

            if len(words) == 2:
                w, _ = Word.objects.get_or_create(
                    current=words[0], 
                    next=words[1]
                )
                w.es_current=shrifts[0]
                w.es_next=shrifts[1]
                w.save()
            elif len(words) == 1:
                w, _ = Word.objects.get_or_create(
                    current=words[0], 
                    next=None
                )
                w.es_current=shrifts[0]
                w.es_next=None
                w.save()
            else:
                w, _ = Word.objects.get_or_create(current=words[0], next=words[1])
                w.es_current=shrifts[0]
                w.es_next=shrifts[1]
                w.save()
                                
                for i in range(1, len(words)-1, 1):
                    w, _ = Word.objects.get_or_create(
                        current=words[i], 
                        next=words[i+1]
                    )
                    w.es_current=shrifts[i]
                    w.es_next=shrifts[i+1]
                    w.save()
                
                w, _ = Word.objects.get_or_create(
                    current=words[-1], 
                    next=None
                )
                w.es_current=shrifts[-1]
                w.es_next=None    
                w.save()
                
            
        return HttpResponse(
            status=200,
            content_type="application/json; charset=utf-8",
        )

    @staticmethod
    def remove_dots(text):

        text = text.encode('utf-8')
        
        for d in D.diacritics:
            text = text.replace(d, b'')
            
        for k, v in D.dotless.items():
            text = text.replace(k, v)
            
        return text.decode('utf-8')

    @staticmethod
    def remove(request):
        objs = Word.objects.all()
        for obj in objs:
            obj.delete()

        return HttpResponse(
            status=200,
            content_type="application/json; charset=utf-8",
        )

    @staticmethod
    def search(request):

        body = json.loads(request.body)
        print("BODY", body)
        text = body.get('text', None)
        rhythms = body.get('rhythms', None)
        keyboard = body.get('keyboard', None)

        data = {
            "rhythms": rhythms,
            "suggestions": None,
            "text": text,
            "is_hamza": False,
        }

        #mode = is_keyboard_changed(mode, text)

        suggestions = WordView._manage_hamza(text, keyboard)
        data['suggestions'] = suggestions

        if len(suggestions) == 1:
            text = change_text(text, suggestions[0])
            data['suggestions'] = []
            data['text'] = text
        elif len(suggestions) > 1:
            data['suggestions'] = suggestions
            data['is_hamza'] = True    
        else:
            if text[-1] == " ":        
                suggestions = WordView._suggest_next_word(text, rhythms)
            else:        
                suggestions = WordView._suggest_next_syllable(text, rhythms)
            
        data['rhythms'] = WordView._suggest_rhythms(text, rhythms)
        return HttpResponse(
            json.dumps({"data": data}),
            status=200,
            content_type="application/json; charset=utf-8",
        )
    
    @staticmethod
    def _suggest_next_syllable(text, rhythms):

        arabic = from_arabic_to_translit(text[1:])
        print("ARABIC", arabic)
        if arabic:
            if len(arabic) >= 3:
                cut = split(arabic)
            else:
                cut = arabic
        else:
            return []

        print("CUT\n", cut)
        syllables = cut.split(' ')
        print("SYLLABLES\n", syllables)
        data = []
        
        if len(syllables) > 1:
            rows = TranslitWord.objects.filter(
                    prev__iexact=syllables[-2], 
                    current__iexact=syllables[-1]
                )
            for row in rows:
                if row.next:
                    data.append(from_translit_to_arabic(row.next))

        else:
            rows = TranslitWord.objects.filter(
                    prev__iexact=syllables[0] 
                )
            for row in rows:
                if row.current:
                    data.append(from_translit_to_arabic(row.current))

        data = sort_by_frequency(data)

        pattern = classify(text)
        
        n = len(pattern)
        
        suggestions = []

        if rhythms == None:
            rhythms = []
            rs = Rhythm.objects.values('name')
            for r in rs:
                rhythms.append(r['name'])

        for rhythm in rhythms:
            r = Rhythm.objects.get(name=rhythm)
            next = r.pattern[n]
            for d in data:
                if len(d) == 1:
                    if next == 1 and n == len(r.pattern) - 1:
                        suggestions.append(d)
                elif classify(d) == next:
                    suggestions.append(d)

        return suggestions
    
    @staticmethod
    def _suggest_rhythms(text, rhythms):
        text = from_arabic_to_translit(text[1:])
        parts = split(text)
        pattern = classify(parts)
        
        if rhythms:
            if rhythms[0].startswith(pattern):
                return rhythms
        
        rhythms = Rhythm.objects.all()
        data = []
        
        for r in rhythms:
            if r.pattern.startswith(pattern):
                data.append(r.name)
    
        return data

    def _suggest_next_word(text, rhythms):
        if rhythms == None:
            rhythms = Rhythm.objects.values('name')

        text = text.strip().split(' ')[-1]
        S, M, L = WordView.get_S_M_L(text)

        cut = split(from_arabic_to_translit(text))

        pattern = classify(cut)
        suggestions = []

        for rhythm in rhythms:
            r = Rhythm.objects.get(name=rhythm)

            if r.pattern.startswith(pattern):
                words = Word.objects.filter(current=text)

                for word in words:
                    SW, MW, LW = WordView.get_S_M_L(word.next)
                    ptr = classify(SW+MW)
                    if r.pattern.startswith(pattern+ptr):
                        tr_word = from_arabic_to_translit(word.next)
                        if not is_vowel(tr_word[0]) and \
                            len(L) == 2 and \
                            not is_vowel(L[0]) and\
                            is_vowel(L[1]):
                            suggestions.append(word.next)
                        elif len(L) == 3 and not is_vowel(L[0]) and is_vowel(L[1]) and is_vowel(L[2]):
                            suggestions.append(word.next)
                        elif len(L) == 3 and not is_vowel(L[0]) and is_vowel(L[1]) and not is_vowel(L[2]):
                            if classify(split(L + SW)) == '12':
                                suggestions.append(word.next)

        return list(set(suggestions))

    def get_S_M_L(text):
        text = apply_transformation_rules(text)
        text = from_arabic_to_translit(text)
        S = ''
        M = ''
        L = ''

        # get first cv index
        i = 0 
        while i < len(text) -1:
            if not is_vowel(text[i]) and is_vowel(text[i+1]):
                break
            else:
                i += 1
        
        # S part
        S = text[:i]

        # get last cv index
        j = len(text) - 1
        while j > 1:
            if is_vowel(text[j]) and not is_vowel(text[j-1]):
                j -= 1
                break
            else:
                j -= 1
        
        # L part
        L = text[j:]  
        
        # M part
        M = text[i:j]

        return S, M, L

    @staticmethod
    def _manage_hamza(text, keyboard):

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

    """
    @staticmethod
    def is_rhythmable(text):
        text = from_arabic_to_translit(text)

        if len(text) < 4:
            return False, 0 
        
        if is_vowel(text[-4]) and is_vowel(text[-3]) and not is_vowel(text[-2]) and is_vowel(text[-1]):
            return True, 4
        
        if is_vowel(text[-4]) and not is_vowel(text[-2]) and is_vowel(text[-1]):
            if text[-3] in 'wy':
                return True, 4
            
        if len(text) > 6:
            if is_vowel(text[-7]) and is_vowel(text[-6]) and not is_vowel(text[-5]) and \
                is_vowel(text[-4]) and not is_vowel(text[-3]) and \
                is_vowel(text[-2]) and is_vowel(text[-1]):
                    return True, 7
            

        return False, 0
    
    @staticmethod
    def suggest_new_line(text):
        b, t = WordView.is_rhythmable(text)

        suggestions = []
        if b:
            suffix = text[-t:]

            rhymes = Word.objects.annotate(
                ending=Right('next', t)
            ).filter(ending=suffix)
    
            suggestions = [w.next for w in rhymes]

        return suggestions
    """

"""
{ pattern: new RegExp(" كَالل", "u"), replace: " كَالل" },

{ pattern: new RegExp(" الل", "u"), replace: " الل" },

{ pattern: new RegExp(" فَالل", "u"), replace: " فَالل" },

{ pattern: new RegExp(" بَِ", "u"), replace: " بِا" },
{ pattern: new RegExp(" فَبَِ", "u"), replace: " فَبِا" },
{ pattern: new RegExp(" وَبَِ", "u"), replace: " وَبِا" },

{ pattern: new RegExp("يِ", "u"), replace: "يّ" },
{ pattern: new RegExp("يِّ", "u"), replace: "يِّ" },
{ pattern: new RegExp("يِّ", "u"), replace: "يِّى" },

{ pattern: new RegExp("وُ", "u"), replace: "وّ" },
{ pattern: new RegExp("وُّ", "u"), replace: "وُّ" },
{ pattern: new RegExp("وُّ", "u"), replace: "وُّو" },

{ pattern: new RegExp(" الُ", "u"), replace: " الو" },
{ pattern: new RegExp(" الِ", "u"), replace: " الي" },
{ pattern: new RegExp(" الءَ", "u"), replace: " الأَ" },

{ pattern: new RegExp(" الءُ", "u"), replace: " الأُ" },
{ pattern: new RegExp(" الءِ", "u"), replace: " الإِ" },
{ pattern: new RegExp(" الل", "u"), replace: " الل" },


{ pattern: new RegExp("َُ", "u"), replace: "َو" },
{ pattern: new RegExp("َِ", "u"), replace: "َي" },
{ pattern: new RegExp("َُ", "u"), replace: "وَ" },
{ pattern: new RegExp("ُِ", "u"), replace: "وِ" },
{ pattern: new RegExp("ُِ", "u"), replace: "ُيُ" },
{ pattern: new RegExp("َِ", "u"), replace: "يَ" },

{ pattern: new RegExp("َاُ", "u"), replace: "َاو" },
{ pattern: new RegExp("َاِ", "u"), replace: "َاي" },
{ pattern: new RegExp("ِيَ", "u"), replace: "ِيَ" },
{ pattern: new RegExp("ِيُ", "u"), replace: "ِيُ" },
{ pattern: new RegExp("ُوَ", "u"), replace: "ُوَ" },
{ pattern: new RegExp("ُوِ", "u"), replace: "ُوِ" },
"""