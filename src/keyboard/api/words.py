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
from ..tools.constants import Diacritics as D
from ..tools.transformation_tools import from_arabic_to_translit, from_translit_to_arabic 
from ..tools.transformation_tools import classify, split, apply_transformation_rules


class WordView(View):

    def get(self, request):
        count = int(request.GET.get("count", None))
        blocks = Koran.objects.filter(id__gt=count*600, id__lt=(count+1)*600-1)
        count = len(blocks)
        j = 0
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
                    next=None,
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
                        next=words[i+1],
                    )
                    w.es_current=shrifts[i]
                    w.es_next=shrifts[i+1]
                    w.save()

                w, _ = Word.objects.get_or_create(
                    current=words[-1], 
                    next=None,
                )
                w.es_current=shrifts[-1],
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
        print("DATA", json.loads(request.body))
        words = json.loads(request.body).get('text', None)
        rhythm = json.loads(request.body).get('rhythms', None)
        mode = json.loads(request.body).get('withDiacritics', None)
        keyboard = json.loads(request.body).get('keyboard')
        text = words
        mode = is_keyboard_changed(mode, text)
        
        new_rhyms = None
        if keyboard == 2:
            data = WordView.manage_hamza(text, phonemic=False)
        else:
            print("AAAAAAAAAA")
            data = WordView.manage_hamza(text)

        if len(data) == 1:
            text = data[0]
            data = []

        else:
            if len(data) == 0:
                if words[-1] == " ":
                    
                    words = words.strip().split(' ')
                    data = []
                    
                    new_rhyms = WordView.suggest_new_line(words[-1])
                    if mode:
                        data = WordView.manage_hamza(text)
                    else:
                        data = WordView.suggest_next_word(words[-1], rhythm)
                    print("SUGGESTED WORDS\n", data)
                    print("SUGGESTED rhyms\n", new_rhyms)
                else:
                    print("TRANSLIT")
                    arabic = from_arabic_to_translit(words[1:])
                    if arabic:
                        print("ARABIC", arabic)
                        if len(arabic) >= 3:
                            cut = split(arabic)
                        else:
                            cut = arabic
                        print("CUT", cut)

                        translits = cut.split(' ')
                        print("TRANSLIT", translits)
                        print("MODE", mode)
                        
                        data = WordView.manage_hamza(words, phonemic=False)
                        if len(data) == 0 and keyboard == 1:
                            data = WordView.suggest_next_syllables(translits, rhythm, mode)
                        

        rhythms = WordView.get_rhythms(text)
        if len(rhythms) and rhythm:
            rhythms = [rhythm]
        

        data = {
            "rhythms": rhythms,
            "suggestions": data,
            "new_rhyms": new_rhyms,
            "text": text,
        }

        return HttpResponse(
            json.dumps({"data": data}),
            status=200,
            content_type="application/json; charset=utf-8",
        )
    
    @staticmethod
    def suggest_next_syllables(cut, rhythm, mode=False):

        data = []
        sort_data = []
        if len(cut) > 1:
            suggestions = TranslitWord.objects.filter(prev__iexact=cut[-2], current__iexact=cut[-1])
            for suggest in suggestions:
                if suggest.next:
                    sort_data.append(suggest.next)
                    res = from_translit_to_arabic(suggest.next)
                    data.append(res)

        text = ' '.join(cut)
        s_data = sort_by_frequency(data)

        pattern = classify(text)
        
        n = len(pattern)
        print("R NAME", rhythm)
        data = []
        if rhythm:
            r = Rhythm.objects.get(name=rhythm)
            next = r.pattern[n]

            for d in s_data:
                if len(d) == 1:
                    if next == 1 and n == len(r.pattern) - 1:
                        data.append(d)
                elif classify(d) == next:
                    data.append(d)

        return data
    
    @staticmethod
    def get_rhythms(text):

        rhythms = Rhythm.objects.all()

        text = from_arabic_to_translit(text)
        parts = split(text)
        pattern = classify(parts)
        n = len(pattern)

        data = []

        for r in rhythms:
            if pattern == r.pattern[:n]:
                data.append(r.name)

        return data

    def suggest_next_word(text, rhythms):

        S, M, L = WordView.get_S_M_L(text)

        cut = split(from_arabic_to_translit(text))

        pattern = classify(cut)
        print("WPATTERN", pattern)
        suggestions = []
        # do this for many rhythms

        if rhythms is None:
            rhythms = []
        if type(rhythms) == str:
            rhythms = [rhythms]
        print("RRRR", rhythms)
        for rhythm in rhythms:
            r = Rhythm.objects.get(name=rhythm)

            if r.pattern.startswith(pattern):
                words = Word.objects.filter(current=text)
                print("IIIIIIIF", r.pattern)
                for word in words:
                    print("WWW", word)
                    SW, MW, LW = WordView.get_S_M_L(word.next)
                    print("SMLW", SW, MW, LW)
                    ptr = classify(SW+MW)
                    print("WWPAT", ptr)
                    if r.pattern.startswith(pattern+ptr):
                        print("IIF RHYTHMS")
                        tr_word = from_arabic_to_translit(word.next)
                        print("TR WORD", tr_word)
                        if not is_vowel(tr_word[0]) and \
                            len(L) == 2 and \
                            not is_vowel(L[0]) and\
                            is_vowel(L[1]):
                            print("SUG IG")
                            suggestions.append(word.next)
                        elif len(L) == 3 and not is_vowel(L[0]) and is_vowel(L[1]) and is_vowel(L[2]):
                            print("SUG elif 1")
                            suggestions.append(word.next)
                        elif len(L) == 3 and not is_vowel(L[0]) and is_vowel(L[1]) and not is_vowel(L[2]):
                            if classify(split(L + SW)) == '12':
                                print("SUG elif 2") 
                                suggestions.append(word.next)

        return suggestions

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

    @staticmethod
    def manage_hamza(text, phonemic=True):

        words = text.split(' ')
        word = WordView.change_hamza(words[-1])
        hmz = HamzaWord.objects.filter(hamza=word)
        
        data = []
        for h in hmz:
            if phonemic:
                data.append(h.phonemic)
            else:
                data.append(h.easy_shrift)
        
        return list(set(data))

    @staticmethod
    def change_hamza(text):
        hamzas = [chr(0x0625), chr(0x0624), chr(0x0623), chr(0x0626), chr(0x0621)]
        for h in hamzas:
            text = text.replace(h, chr(0x0621))

        return text


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