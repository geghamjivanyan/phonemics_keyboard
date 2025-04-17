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