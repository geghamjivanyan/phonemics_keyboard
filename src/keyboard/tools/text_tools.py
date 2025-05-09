#
#from .utils import is_vowel

vowels = 'aiuAYNW*'
#
def is_vowel(letter):
    """
    check if letter is vowel

    :params letter - letter which should be checked

    :returns: True or False
    """
    return letter in vowels



class TextManager:
    def __init__(self, txt):
        self.text = txt

    def _is_cvcc(self, text):

        return not is_vowel(text[0]) and \
            is_vowel(text[1]) and \
            not is_vowel(text[2]) and\
            not is_vowel(text[2])


    def _is_cvvv(self, text):

        return not is_vowel(text[0]) and \
            is_vowel(text[1]) and \
            is_vowel(text[2]) and\
            is_vowel(text[2])


    def _is_cv(self, text):

        return not is_vowel(text[0]) and \
            is_vowel(text[1])

    def split_to_phonems(self):
        txt = ''
        i = 0
        is_two = False
        while i < len(self.text)-2:
            if self._is_cvcc(self.text[i:i+4]):
                is_two = True
                txt += self.text[i:i+4]
                txt += ' '
                i += 4
            elif self._is_cvvv(self.text[i:i+4]):
                is_two = True
                txt += self.text[i:i+4]
                txt += ' '
                i += 4
            elif self._is_cv(self.text[i:i+2]):
                is_two = False
                txt += self.text[i:i+2]
                txt += ' '
                i += 2
            else:
                print("DDDD", i)
        if is_two:
            if self._is_cv(self.text[i:i+2]):
                txt += self.text[i:i+2]

        return txt 


                
