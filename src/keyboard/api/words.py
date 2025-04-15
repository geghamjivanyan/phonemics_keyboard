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

from ..tools.utils import is_vowel, sort_by_frequency
from ..tools.constants import Diacritics as D
from ..tools.transformation_tools import from_arabic_to_translit, from_translit_to_arabic 
from ..tools.transformation_tools import classify


class WordView(View):

    def get(self, request):
        blocks = Koran.objects.all()
        count = len(blocks)
        j = 0
        for block in blocks:
            words = block.arabic.split(' ')
            if len(words) == 2:
                Word.objects.get_or_create(
                    current=words[0], 
                    next=words[1],
                    es_current=WordView.remove_dots(words[0]),
                    es_next=WordView.remove_dots(words[1]), 
                )
            elif len(words) == 1:
                Word.objects.get_or_create(
                    current=words[0], 
                    next=None,
                    es_current=WordView.remove_dots(words[0]),
                    es_next=None
                )
            else:
                Word.objects.get_or_create(current=words[0], next=words[1])
                for i in range(1, len(words)-1, 1):
                    Word.objects.get_or_create(
                        current=words[i], 
                        next=words[i+1],
                        es_current=WordView.remove_dots(words[0]),
                        es_next=WordView.remove_dots(words[1]),
                    )

                Word.objects.get_or_create(
                    current=words[-1], 
                    next=None,
                    es_current=WordView.remove_dots(words[-1]),
                    es_next=None    
                )
            
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
        text = words
        print("WORD", words)
        
        new_rhyms = None
        if words[-1] == " ":
            
            words = words.strip().split(' ')
            data = []
            data = WordView.suggest_next_word(words[-1], rhythm)
            new_rhyms = WordView.suggest_new_line(words[-1])
            print("SUGGESTED WORDS\n", data)
            print("SUGGESTED rhyms\n", new_rhyms)
        else:
            print("TRANSLIT")
            arabic = from_arabic_to_translit(words)
            if arabic:
                print("ARABIC", arabic)
                if len(arabic) >= 3:
                    cut = WordView.split(arabic)
                else:
                    cut = arabic
                print("CUT", cut)

                translits = cut.split(' ')
                print("TRANSLIT", translits)
                data = WordView.suggest(translits, rhythm)

        if rhythm:
            rhythms = [rhythm]
        else:
            rhythms = WordView.get_rhythms(text)
        data = {
            "rhythms": rhythms,
            "suggestions": data,
            "new_rhyms": new_rhyms,
        }

        return HttpResponse(
            json.dumps({"data": data}),
            status=200,
            content_type="application/json; charset=utf-8",
        )
    
    @staticmethod
    def suggest(cut, rhythm):

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
        print("TEXT", text)
        parts = WordView.split(text)

        pattern = classify(parts)

        n = len(pattern)

        data = []

        for r in rhythms:
            if pattern == r.pattern[:n]:
                data.append(r.name)

        return data


    @staticmethod
    def split(res):
        s = ''
        i = 0

        res = res.replace('L', 'l')
        # arrange the case when text len is <= 4

        if len(res) == 3:
            if is_vowel(res[i]) and is_vowel(res[i+1]) and not is_vowel(res[i+2]):
                return res[:2] + ' ' + res[2]
            elif not is_vowel(res[i]) and not is_vowel(res[i+1]):
                if not(is_vowel(res[2]) and res[i] != res[i+1]):
                    return res[0] + ' ' + res[1:]
            elif not is_vowel(res[i]) and not is_vowel(res[i+1]):
                if not(is_vowel(res[2]) and res[i] == res[i+1]):
                    return res
            elif is_vowel(res[i]) and not is_vowel(res[i+1]) and is_vowel(res[i+2]):
                return res[0] + ' ' + res[1:]
            
        res = res + '++'
        while i < len(res)-2:
            # after vv if vvc 
            if is_vowel(res[i]) and is_vowel(res[i+1]) and not is_vowel(res[i+2]):
                s += res[i:i+2] + ' '
                i += 2
            # after c1 if c1c2v and c1 != c2
            elif not is_vowel(res[i]) and not is_vowel(res[i+1]):
                if not(is_vowel(res[2]) and res[i] != res[i+1]): 
                    s += res[i] + ' '
                    i += 1
            # before c1 if c1c2v and c1 = c2
            elif not is_vowel(res[i]) and not is_vowel(res[i+1]):
                if not(is_vowel(res[2]) and res[i] == res[i+1]): 
                    s += ' ' + res[i:i+2]
                    i += 1 
            # before c2 if v1c2v2 
            elif is_vowel(res[i]) and not is_vowel(res[i+1]) and is_vowel(res[i+2]):
                s += res[i] + ' '
                i+=1 
            else:
                s += res[i]
                i += 1
        
        return s.strip()


    """
    We need to write a new code for suggesting words in poerty composition. User types first word, so we have to continuously evaluate the Prosodic Metre of the typed text, and to know the Metre of the words before suggesting them. Therefore:
    1 For X =  (ث ص ض ن ت س ش ر ز د ذ ط ظ)
    2 For C = (ج ح خ ه ع غ ف ق ك م ل و ي ء)

    1 The first word or syllable is styped by the User.
    2 If the word starts with:
        1 (ا) : (ءَ)
        2 (ال) + X : (ءَ) + XX
        3 (هؤلاء) and other words turned phonemic
        4 (ُوا) : (ُو)
        End of word 5 Tanween : (a, A, u, i"ُو") + n
        6 With the above the first word is phonemic and can be split into syllables.
        7 Adding a tanween to a word will transform the last long syllable, (..2):(..12)
        8 No word starting with (ال) can end with Tanween
        9 Rule A: (“َ ا” = “َ”)، (“َا ا”=“َ”), (“ُ ا”=“ُ”), (“ُوا ا”=“ُ”), (“ِ ا”=“ِ”), (“ِي ا”=“ِ”), (“َى ا”=“َ”)
        10 After first word, any word will be weighed Metrically without first (ا)
        11 For the words A=(" فَ"، " وَكَ"، " كَ"، " فَكَ"،" كَبِ"، " وَ"،" فَوَ"، " وَبِ"، " بِ"، " أَبِ"، " فَبِ"):
        1 (A) + (ال): (A) + (“ ”) + (ال)"
    """
    
    @staticmethod
    def apply_transformation_rules(text):

        print("BEFORE", text)
    
        X = ["ث", "ص", "ض", "ن", "ت", "س", "ش", "ر", "ز", "د", "ذ", "ط", "ظ"]
        C = ["ج", "ح", "خ", "ه", "ع", "غ", "ف", "ق", "ك", "م", "ل", "و", "ي", "ء"]

        #  1 (ا) : (ءَ) +
        if text[0] == "ا":
            text = "ءَ" + text[1:]
        
        # 2 (ال) + X : (ءَ) + XX  +
        for x in X:
            term = "ال" + x
            if text.startswith(term):
                start = "ءَ" + x + x
                text = start + text[len(term)]

        mapping = {
            "هَذا": "هَاذا",
            "الرَّحْمَنِ": "ارْرَحْمَانِ",
            "أُولَئِكَ": "أُلَائِكَ",
            "هَؤُلَاء": "هَاؤُلَاء",
            "سَمَوَات": "سَمَاوَات",
            "الله": "اللاه",
            "اللَه": "الْلاه",
            "اللَّه": "الْلاه",
            "لِلَّهِ": "لِلْلَاهِ",
            "الَّذِي": "الْلَذِي",
            "الَّذِينَ": "الْلَذِينَ",
            "لِلَّذِي": "لِلْلَذِي"
        }
        # 3 (هؤلاء) and other words turned phonemic  +
        for m in mapping:
            if text.startswith(m):
                text = mapping[m] + text[len(m):]

        # 4 "ُوا" : "ُو"

        if text.endswith("ُوا"):
            text = text[:-len("ُوا")] + "ُو"

        # 5 (a, A, u, i) + n
        vowels = [chr(0x064E), chr(0x0650), chr(0x064F)]
        for v in vowels:
            if text.endswith(v + " "):
                text = text[:-1] + chr(0x0646) + " "

        # 

        TR = {
            "َ ا": "َ",
            "َا ا": "َ",
            "ُ ا": "ُ",
            "ُوا ا": "ُ",
            "ِ ا": "ِ",
            "ِي ا": "ِ",
            "َى ا": "َ"
        }
        # 9 Rule A: (“َ ا” = “َ”)، (“َا ا”=“َ”), (“ُ ا”=“ُ”), (“ُوا ا”=“ُ”), (“ِ ا”=“ِ”), (“ِي ا”=“ِ”), (“َى ا”=“َ”)
        for a in TR:
            text = text.replace(a, TR[a])

        # 11 For the words A=(" فَ"، " وَكَ"، " كَ"، " فَكَ"،" كَبِ"، " وَ"،" فَوَ"، " وَبِ"، " بِ"، " أَبِ"، " فَبِ")
        # (A) + (ال): (A) + (“ ”) + (ال)"
        A = ["فَ", "وَكَ", "كَ", "فَكَ", "كَبِ", "وَ", "فَوَ", "وَبِ", "بِ", "أَبِ", "فَبِ"]

        for a in A:
            text = text.replace(a + "ال", a + " " + "ال")


        print("AFTER", text)

        return text

    """
    we will split every word into 3 parts:
    Start  S- part before first cv
    Middle M- part from first cv until but not include last cv
    Last   L- starts last cv
    
    if we have a desired rhythm R = [DEFGHIJK]
    for first word:
        if S+M+l has n number of syllables equal in length as first n intries in R:
        any word starting with a consonant is a suggestion option 
        if its m number of syllables has same lengths as the next m entries in R after the nth entry

    R = [DEFGHIJK]
    L last word
    S next word
    M next word

    last letter in last word
    next word starts with a transitional vowel
    if words always start with a consonant, we calculate the words as they r


    L can be c1v1, or c1v1v2, or c1v1c2
    when S of next word is V5C5 c6v6..
    c1v1 + V5C5c6v6 = c1v1C5 + c6v6..
    c1v1v2+ V5C5c6v6 = c1v1C5 + c6v6..
    c1v1c2 + V5C5c6v6 =c1v1 + c2V5C5 +c6v6..

    c1v1 + V5C5 = c1v1C5       
    c1v1v2+ V5C5 = c1v1C5 
    c1v1c2 + V5C5 = c1v1 + c2V5C5
    """
    def suggest_next_word(text, rhythms):

        S, M, L = WordView.get_S_M_L(text)

        cut = WordView.split(from_arabic_to_translit(text))

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
                            if classify(WordView.split(L + SW)) == '12':
                                print("SUG elif 2") 
                                suggestions.append(word.next)

        return suggestions

    def get_S_M_L(text):
        text = WordView.apply_transformation_rules(text)
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
    
    """
    1- We always get cvv. at the end, even if its cv.
    2- Before CV. We we can get any of:
    • VV                                              VVCV.
    • AW or AY                                VwCV. Or VyCV.
    • VVcv                                         VVcvCV.

    So we have cases for ends with:
    • 21 or 22: in both cases will have vvcv. Or vvcvv.
    • Or we can have zxcv. Or zxcvv. Where x=(w, y) z=(a,A,i,u)
    • 212 or 211 vvcvCV. Or vvcvCVV. 
    fdg hgj hgjk maanila  > maanilaa > cvv cv cvv.
                  saa ni laa
    vvcv.
    vXcv.   x=wy
    vvcvcvv.
    
    always ends with cv or cvv, always cv=cvv
    go to vv or vw or vy before that
    
    u will need any word, or words that end up with the above syllables
        """
    @staticmethod
    def is_rhythmable(text):
        text = from_arabic_to_translit(text)

        if len(text) < 4:
            return False 
        
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
    @staticmethod
    def new_line(text):
        text = WordView.apply_transformation_rules(text)
        text = from_arabic_to_translit(text)

        cut = WordView.split(text)

        # pattern of text
        pattern = classify(cut)

        # pattern of last word
        lp = classify(last)

        # pattern without last word 
        rp = pattern[:-len(lp)]

        lines = []
        for rhyme in rhymes:
            line = ''
            ptr = classify(rhyme.current + rhyme.next)
            if pattern.endswith(ptr):
                line = rhyme.current + ' ' + rhyme.next

        return lines  
    """

    """
    we need to work out the easy shrift typing, and suggestions for easy shrift (in full dots and diacritics)
    1- we type in easy shrift, get suggestions in full text
    2- as we switch between easy shrift and phonemic keyboards, the same text changes between easy shrift and full text
    if we do not have the word in full text, no suggestion is given
    """

