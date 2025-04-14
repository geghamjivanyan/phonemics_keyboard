#
import json

#
from datetime import datetime
from collections import Counter

#
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.db.models import Value
from django.db.models.functions import Right

from ..models.words import Word
from ..models.koran import Koran
from ..models.translit_words import TranslitWord
from ..models.rhythms import Rhythm

#
def is_vowel(letter):
    """
    check if letter is vowel

    :params letter - letter which should be checked

    :returns: True or False
    """
    vowels = 'aiuAYNW*'
    return letter in vowels

class WordView(View):

    def get(self, request):
        blocks = Koran.objects.all()
        count = len(blocks)
        j = 0
        for block in blocks:
            if j % 100 == 0:
                print("J", j, "out of", count)
            words = block.arabic.split(' ')
            #words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh']
            if len(words) == 2:
                Word.objects.get_or_create(current=words[0], next=words[1])
            elif len(words) == 1:
                Word.objects.get_or_create(current=words[0], next=None)
            else:
                Word.objects.get_or_create(current=words[0], next=words[1])
                for i in range(1, len(words)-1, 1):
                    next=words[i+1]
                    current = words[i]
                    Word.objects.get_or_create(
                        current=current, 
                        next=next
                    )


                Word.objects.get_or_create(current=words[-1], next=None)
            
        return HttpResponse(
            status=200,
            content_type="application/json; charset=utf-8",
        )

    @staticmethod
    def easy_shrift(request):

        words = Word.objects.all()
        count = len(words)
        i = 0
        for word in words:
            if i % 100 == 0:
                print(i, "out of", count)
            i+=1
            word.prev = WordView.remove_d(word.prev)
            if word.current:
                word.current = WordView.remove_d(word.current)
            if word.next:
                word.next = WordView.remove_d(word.next)

            word.save()

        return HttpResponse("OK")        

    @staticmethod
    def remove_d(text):

        text = text.encode('utf-8')

        diacritics = [
            chr(0x064F).encode('utf-8'),  
            chr(0x064E).encode('utf-8'), 
            chr(0x064D).encode('utf-8'), 
            chr(0x064C).encode('utf-8'), 
            chr(0x064B).encode('utf-8'),
            chr(0x0651).encode('utf-8'), 
            chr(0x0650).encode('utf-8'),
            chr(0x0652).encode('utf-8'), 
        ]

        dotless = {
            chr(0x0628).encode('utf-8'): chr(0x066E).encode('utf-8'),
            chr(0x062A).encode('utf-8'): chr(0x066E).encode('utf-8'),
            chr(0x062B).encode('utf-8'): chr(0x066E).encode('utf-8'),
            chr(0x062C).encode('utf-8'): chr(0x062D).encode('utf-8'),
            chr(0x062E).encode('utf-8'): chr(0x062D).encode('utf-8'),
            chr(0x0630).encode('utf-8'): chr(0x062F).encode('utf-8'),
            chr(0x0632).encode('utf-8'): chr(0x0631).encode('utf-8'),
            chr(0x0634).encode('utf-8'): chr(0x0633).encode('utf-8'),
            chr(0x0636).encode('utf-8'): chr(0x0635).encode('utf-8'),
            chr(0x0638).encode('utf-8'): chr(0x0637).encode('utf-8'),
            chr(0x063A).encode('utf-8'): chr(0x0639).encode('utf-8'),
            chr(0x0629).encode('utf-8'): chr(0x0647).encode('utf-8'),
        }
        
        for d in diacritics:
            text = text.replace(d, b'')
            
        for k, v in dotless.items():
            text = text.replace(k, v)
            
        return text.decode('utf-8')


    @staticmethod
    def _remove_dots(text):
        is_change = False
        text += '*'
        dots = {
            chr(0x062D).encode("utf-8") + b'.': chr(0x062E).encode("utf-8"),
            chr(0x062E).encode("utf-8") + b'.': chr(0x062C).encode("utf-8"),
            chr(0x066E).encode("utf-8") + b'.': chr(0x0628).encode("utf-8"),
            chr(0x0628).encode("utf-8") + b'.': chr(0x062A).encode("utf-8"),
            chr(0x0646).encode("utf-8") + b'.': chr(0x062A).encode("utf-8"),
            chr(0x0647).encode("utf-8") + b'.': chr(0x0629).encode("utf-8"),
            chr(0x064E).encode("utf-8") + b'.': chr(0x064B).encode("utf-8"),
            chr(0x064F).encode("utf-8") + b'.': chr(0x064C).encode("utf-8"),
            chr(0x0650).encode("utf-8") + b'.': chr(0x064D).encode("utf-8"),
            chr(0x0631).encode("utf-8") + b'.': chr(0x0632).encode("utf-8"),
            chr(0x062F).encode("utf-8") + b'.': chr(0x0630).encode("utf-8"),
            chr(0x062A).encode("utf-8") + b'.': chr(0x062B).encode("utf-8"),
            chr(0x0637).encode("utf-8") + b'.': chr(0x0638).encode("utf-8"),
            chr(0x0633).encode("utf-8") + b'.': chr(0x0634).encode("utf-8"),
            chr(0x0635).encode("utf-8") + b'.': chr(0x0636).encode("utf-8"),
            chr(0x0639).encode("utf-8") + b'.': chr(0x063A).encode("utf-8"),
        }
        txt = ''
        i = 0
        while i < len(text)-1:
            if text[i:i+2].encode('utf-8') in dots:
                print("LETTER", text[i:i+2])
                txt += dots[text[i:i+2].encode('utf-8')].decode("utf-8")
                i += 2
                is_change = True 
            else:
                txt += text[i]
                i += 1

        return txt, is_change
    
    @staticmethod
    def remove_dots(request):
        text = 'ح..'
        txt = text
        is_change = True

        while is_change:
            print("AAAAA")
            text, is_change = WordView._remove_dots(text)

        return HttpResponse("Before {} -> After {}".format(txt, text))


    @staticmethod
    def remove(request):
        objs = Word.objects.all()
        for obj in objs:
            obj.delete()

        return HttpResponse("OK")

    @staticmethod
    def search(request):
        print("DATA", json.loads(request.body))
        words = json.loads(request.body).get('text', None)
        rhythm = json.loads(request.body).get('rhythms', None)
        text = words
        print("WORD", words)
        #words = words.replace('_', ' ')
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
            arabic = WordView._from_arabic_to_translit(words)
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
    def _from_translit_to_arabic(text):

        translit = {
            'aa': chr(0x064E) + chr(0x0627),
            'AA': chr(0x064E) + chr(0x0627),
            'ii': chr(0x0650) + chr(0x064A),
            'uu': chr(0x064F) + chr(0x0648),
            'A':  chr(0x064E),
            'a':  chr(0x064E),
            'i':  chr(0x0650),
            'u':  chr(0x064F),
            'ʼ':  chr(0x0621),
            'ʻ':  chr(0x0639),
            'b':  chr(0x0628),
            't':  chr(0x062A),
            'd':  chr(0x062F),
            'ǧ':  chr(0x062C),
            'r':  chr(0x0631),
            'ṯ':  chr(0x062B),
            'z':  chr(0x0632),
            's':  chr(0x0633),
            'ḥ':  chr(0x062D),
            'ḫ':  chr(0x062E),
            'ḏ':  chr(0x0630),
            'ṣ':  chr(0x0635),
            'š':  chr(0x0634),
            'ḍ':  chr(0x0636),
            'ẓ':  chr(0x0638),
            'ṭ':  chr(0x0637),
            'ġ':  chr(0x063A),
            'f':  chr(0x0641),
            'q':  chr(0x0642),
            'k':  chr(0x0643),
            'l':  chr(0x0644),
            'L':  chr(0x0644),
            'm':  chr(0x0645),
            'n':  chr(0x0646),
            'h':  chr(0x0647),
            'w':  chr(0x0648),
            'y':  chr(0x064A),
            ' ': ' ',
        }

        s = ''
        i = 0
        while i < len(text):

            if text[i:i+2] in translit:
                s += translit[text[i:i+2]]
                i += 2
            else:
                try:
                    s += translit[text[i]]
                except KeyError:
                    pass
                i += 1

        return s
    
    @staticmethod
    def _from_arabic_to_translit(text):

        text = text.replace('N', '').replace('Y', '').replace('W', '')

        translit = {
            chr(0x0626): chr(0x02bc), 
            chr(0x0625): chr(0x02bc), 
            chr(0x0623): chr(0x02bc), 
            chr(0x0624): chr(0x02bc),
            chr(0x0621): chr(0x02bc),
            chr(0x064E) + chr(0x064E): 'aa', 
            chr(0x0622): chr(0x02bc) + 'aa',
            chr(0x064E) + chr(0x0627): 'aa',
            chr(0x064E) + chr(0x0649): 'aa',
            #chr(0x064E) + chr(0x0627): 'AA',
            chr(0x0650) + chr(0x064A): 'ii',
            chr(0x064F) + chr(0x0648): 'uu',
            chr(0x064E): 'a',
            chr(0x0650): 'i',
            chr(0x064F): 'u',
            chr(0x0639): 'ʻ',
            chr(0x0628): 'b',
            chr(0x062A): 't',
            chr(0x062F): 'd',
            chr(0x062C): 'ǧ',
            chr(0x0631): 'r',
            chr(0x062B): 'ṯ',
            chr(0x0632): 'z',
            chr(0x0633): 's',
            chr(0x062D): 'ḥ',
            chr(0x062E): 'ḫ',
            chr(0x0630): 'ḏ',
            chr(0x0635): 'ṣ',
            chr(0x0634): 'š',
            chr(0x0636): 'ḍ',
            chr(0x0638): 'ẓ',
            chr(0x0637): 'ṭ',
            chr(0x063A): 'ġ',
            chr(0x0641): 'f',
            chr(0x0642): 'q',
            chr(0x0643): 'k',
            chr(0x0644): 'l',
            #chr(0x0644): 'L',
            chr(0x0645): 'm',
            chr(0x0646): 'n',
            chr(0x0647): 'h',
            chr(0x0648): 'w',
            chr(0x064A): 'y',
            ' ': ' ',
        }
        a_rules = 'Lrqṣṭġḍḍḫ'
        l_rules = 'uaALLAAh'

        s = ''
        i = 0

        #we have letter 0627:
        #  if at the very beginning of text, then: 0627 = 02bc + 064E


        if text[0] == chr(0x0627):
            s += chr(0x2bc) + chr(0x064E)
            i += 1

        while i < len(text):
            if i < len(text) - 1 and text[i+1] == chr(0x0651):
                s += 2*translit[text[i]]
                i+=2 

            if i < len(text) - 1:
                if text[i-1] == ' ' and text[i] == chr(0x0627):
                    s += ' '
                    i += 1
                
            if text[i:i+2] in translit:
                if i > 1 and translit.get(text[i-1], None) and translit[text[i-1]] in a_rules and \
                        text[i] == chr(0x064E):
                        s += 'A'
                        i += 1
                else:
                    s += translit[text[i:i+2]]
                    i += 2
            else:
                try:
                    if i > 0 and text[i-1] == chr(0x064E) and text[i] == chr(0x0627):
                        s += 'a'
                    elif i > 0 and translit.get(text[i-1], None) and translit[text[i-1]] in a_rules and \
                        text[i] == chr(0x064E):
                        s += 'A'
                    elif i > 0 and translit.get(text[i-1], None) and translit[text[i-1]] in l_rules and \
                        text[i] == chr(0x0644):
                        s += 'L'
                    else:
                        s += translit[text[i]]
                except KeyError as err:
                    print("KeyError", err)
                i += 1

            if s[-2:] == 'aA':
                s = s.replace('aA', 'aa')
            elif s[-2:] == 'Aa':
                s = s.replace('Aa', 'AA')

        return s 
    
    @staticmethod
    def suggest(cut, rhythm):

        data = []
        sort_data = []
        if len(cut) > 1:
            suggestions = TranslitWord.objects.filter(prev__iexact=cut[-2], current__iexact=cut[-1])
            for suggest in suggestions:
                if suggest.next:
                    sort_data.append(suggest.next)
                    res = WordView._from_translit_to_arabic(suggest.next)
                    data.append(res)

        text = ' '.join(cut)
        s_data = WordView.sort_by_frequency(data)

        pattern = WordView.classify(text)
        
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
                elif WordView.classify(d) == next:
                    data.append(d)

        return data
    
    @staticmethod
    def sort_by_frequency(lst):
        freq = Counter(lst)
        return sorted(set(lst), key=lambda x: freq[x], reverse=True)
    
    @staticmethod
    def get_rhythms(text):

        rhythms = Rhythm.objects.all()

        text = WordView._from_arabic_to_translit(text)
        print("TEXT", text)
        parts = WordView.split(text)

        pattern = WordView.classify(parts)

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
    
    @staticmethod
    def classify(text):
        #print("CLASS 1", text)
        text = text.split(' ')
        #print("CLASS 2", text)
        pattern = ''
        for txt in text:
            if len(txt) == 0:
                continue
            if len(txt) <= 2:
                pattern += '1'
            elif len(txt) == 3:
                pattern += '2'
            else:
                pattern += '3'

        return pattern

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

        cut = WordView.split(WordView._from_arabic_to_translit(text))

        pattern = WordView.classify(cut)
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
                    ptr = WordView.classify(SW+MW)
                    print("WWPAT", ptr)
                    if r.pattern.startswith(pattern+ptr):
                        print("IIF RHYTHMS")
                        tr_word = WordView._from_arabic_to_translit(word.next)
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
                            if WordView.classify(WordView.split(L + SW)) == '12':
                                print("SUG elif 2") 
                                suggestions.append(word.next)

        return suggestions

    def get_S_M_L(text):
        text = WordView.apply_transformation_rules(text)
        text = WordView._from_arabic_to_translit(text)
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
        text = WordView._from_arabic_to_translit(text)

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

    @staticmethod
    def new_line(text):
        text = WordView.apply_transformation_rules(text)
        text = WordView._from_arabic_to_translit(text)

        cut = WordView.split(text)

        # pattern of text
        pattern = WordView.classify(cut)

        # pattern of last word
        lp = WordView.classify(last)

        # pattern without last word 
        rp = pattern[:-len(lp)]

        lines = []
        for rhyme in rhymes:
            line = ''
            ptr = WordView.classify(rhyme.current + rhyme.next)
            if pattern.endswith(ptr):
                line = rhyme.current + ' ' + rhyme.next

        return lines  


    """
    we need to work out the easy shrift typing, and suggestions for easy shrift (in full dots and diacritics)
    1- we type in easy shrift, get suggestions in full text
    2- as we switch between easy shrift and phonemic keyboards, the same text changes between easy shrift and full text
    if we do not have the word in full text, no suggestion is given
    """

