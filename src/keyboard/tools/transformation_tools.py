from .utils import is_vowel
from .constants import Translit as T


def from_translit_to_arabic(text):
        s = ''
        i = 0
        while i < len(text):

            if text[i:i+2] in T.from_translit:
                s += T.from_translit[text[i:i+2]]
                i += 2
            else:
                try:
                    s += T.from_translit[text[i]]
                except KeyError:
                    pass
                i += 1

        return s
    
def from_arabic_to_translit(text):

        text = text.replace('N', '').replace('Y', '').replace('W', '')

        s = ''
        i = 0

        if text[0] == chr(0x0627):
            s += chr(0x2bc) + chr(0x064E)
            i += 1

        while i < len(text):
            if i < len(text) - 1:
                if text[i+1] == chr(0x0651):
                    s += 2*T.to_translit[text[i]]
                    i+=2 

                elif text[i-1] == ' ' and text[i] == chr(0x0627):
                    s += ' '
                    i += 1
                
            if text[i:i+2] in T.to_translit:
                if i > 1 and T.to_translit.get(text[i-1], None) and T.to_translit[text[i-1]] in T.a_rules and \
                        text[i] == chr(0x064E):
                        s += 'A'
                        i += 1
                else:
                    s += T.to_translit[text[i:i+2]]
                    i += 2
            else:
                try:
                    if i > 0 and text[i-1] == chr(0x064E) and text[i] == chr(0x0627):
                        s += 'a'
                    elif i > 0 and T.to_translit.get(text[i-1], None) and T.to_translit[text[i-1]] in T.a_rules and \
                        text[i] == chr(0x064E):
                        s += 'A'
                    elif i > 0 and T.to_translit.get(text[i-1], None) and T.to_translit[text[i-1]] in T.l_rules and \
                        text[i] == chr(0x0644):
                        s += 'L'
                    else:
                        s += T.to_translit[text[i]]
                except KeyError as err:
                    print("KeyError", err)
                except IndexError as err:
                    print("IndexError", err)
                i += 1

            if s[-2:] == 'aA':
                s = s.replace('aA', 'aa')
            elif s[-2:] == 'Aa':
                s = s.replace('Aa', 'AA')

        return s 

def classify(text):
    text = text.split(' ')
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

def split(res):
        s = ''
        i = 0

        res = res.replace('L', 'l')
        # arrange the case when text len is <= 4

        if len(res) == 3:
            #vvc
            if is_vowel(res[i]) and is_vowel(res[i+1]) and not is_vowel(res[i+2]):
                return res[:2] + ' ' + res[2]
            #c1c2v
            elif not is_vowel(res[i]) and not is_vowel(res[i+1]):
                if not(is_vowel(res[2]) and res[i] != res[i+1]):
                    return res[0] + ' ' + res[1:]
            #c1c2c3
            elif not is_vowel(res[i]) and not is_vowel(res[i+1]):
                if not(is_vowel(res[2]) and res[i] == res[i+1]):
                    return res
            # vcv
            elif is_vowel(res[i]) and not is_vowel(res[i+1]) and is_vowel(res[i+2]):
                return res[0] + ' ' + res[1:]
            
        res = res + '++'
        while i < len(res)-2:
            # after vv if vvc 
            if is_vowel(res[i]) and is_vowel(res[i+1]) and not is_vowel(res[i+2]):
                s += res[i:i+2] + ' '
                i += 2
            # after c1 if c1c2v and c1 != c2
            elif not is_vowel(res[i]) and not is_vowel(res[i+1]) and is_vowel(res[i+2]) and res[i] != res[i+1]:
                s += res[i] + ' '
                i += 1
            # before c1 if c1c2v and c1 = c2
            elif not is_vowel(res[i]) and not is_vowel(res[i+1]) and is_vowel(res[i+2]) and res[i] == res[i+1]:
                s += ' ' + res[i:i+2]
                i += 2
            # before c2 if v1c2v2 
            elif is_vowel(res[i]) and not is_vowel(res[i+1]) and is_vowel(res[i+2]):
                s += res[i] + ' '
                i+=1 
            else:
                s += res[i]
                i += 1
        
        return s.strip()

def apply_transformation_rules(text):
    
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

        return text