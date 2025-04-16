
#

class Constants:
    """
    Constant object for having all necessary constants in one place

    :param vowels - string containing all vowels
    :param consonants - string containig all consonants
    :param plosives - string containing all plosives
    :param s_letters - all letters as string
    :param l_letters - all letters as list
    :param d_letters - all letters as dictionary - {letter-index}
    :param support_weights - dictionary for support weights
    :param friends - friend letters list , the x-axis supports the y-axis
    """

    vowels = 'aiuAYNW*'
    consonants = '.bdfhklmnoqrstwyzġšǧʻʼḍḏḥḫṣṭṯẓL'
    plosives = 'ʼqṭbǧdkt'
    s_letters = '.abdfhiklmnoqrstuwyzġšǧʻʼḍḏḥḫṣṭṯẓ*ALNWY'
    l_letters = [
                  '.', 'a', 'b', 'd', 'f', 'h', 'i', 'k',
                  'l', 'm', 'n', 'o', 'q', 'r', 's', 't',
                  'u', 'w', 'y', 'z', 'ġ', 'š', 'ǧ', 'ʻ',
                  'ʼ', 'ḍ', 'ḏ', 'ḥ', 'ḫ', 'ṣ', 'ṭ', 'ṯ',
                  'ẓ', '*', 'A', 'L', 'N', 'W', 'Y'
                ]
    d_letters = {
                  '.': 0, 'a': 1, 'b': 2, 'd': 3, 'f': 4,
                  'h': 5, 'i': 6, 'k': 7, 'l': 8, 'm': 9,
                  'n': 10, 'o': 11, 'q': 12, 'r': 13, 's': 14,
                  't': 15, 'u': 16, 'w': 17, 'y': 18, 'z': 19,
                  'ġ': 20, 'š': 21, 'ǧ': 22, 'ʻ': 23, 'ʼ': 24,
                  'ḍ': 25, 'ḏ': 26, 'ḥ': 27, 'ḫ': 28, 'ṣ': 29,
                  'ṭ': 30, 'ṯ': 31, 'ẓ': 32, '*': 33, 'A': 34,
                  'L': 35, 'N': 36, 'W': 37, 'Y': 38, 'F': 4
                }
    support_weights = {
                        0: 3, 1: 5, 2: 8, 3: 11, 4: 15,
                        5: 20, 6: 30, 7: 40, 8: 50, 9: 60
                      }
    friends = [
                '''
                _ b d k q r t ǧ ṭ l L ġ
                b _ 4 . 4 . . 4 4 . . 4
                d 4 _ . 4 . 4 4 4 . . 4
                k . . _ 3 . . . . . . 3
                q 4 4 4 _ . . 4 4 . . 5
                r . . . . _ . . . 4 2 .
                t . 4 . . . _ . 4 . . .
                ǧ 4 4 . 4 . . _ 4 . . .
                ṭ 4 4 . 4 . 4 4 _ . . .
                l . . . . 4 . . . _ 4 .
                L . . . . 4 . . . 4 _ .
                ġ . . 3 5 1 1 . . . . _
                ''',
                '''
                _ a A * i y Y u w W
                a _ 5 4 . . . . . .
                A 7 _ 4 . . . . . .
                * 4 4 _ . . . 3 . .
                i . . . _ 3 3 . . .
                y . . . 3 _ 5 . . .
                Y . . . 6 5 _ . . .
                u . 3 . . . . _ 3 3
                w . . . . . . 5 _ 4
                W . . . . . . 3 2 _
                ''',
                '''
                _ m n N w h ʼ ḥ h ḫ d ḏ ẓ l
                m _ 3 2 . . . . . . . . . .
                n 3 _ 4 . . . . . . . . . 3
                N 2 4 _ . . . . . . . . . .
                w . . . _ 3 3 . . . . . . .
                h . . . 3 _ 3 3 . 4 . . . .
                ʼ . . . 3 3 _ . 4 4 . . . .
                ḥ . . . . 3 . _ 4 4 . . . .
                h . . . . . 4 4 _ 4 . . . .
                ḫ . . . . 4 4 4 4 _ . . . .
                d . . . . . . . . . _ 4 . .
                ḏ . . . . . . . . . . _ 4 .
                ẓ . . . . . . . . . . 4 _ .
                l . 3 . . . . . . . . . . _
                '''
              ]


class Diacritics:
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

class Translit:

  from_translit = {
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

  to_translit = {
            chr(0x0626): chr(0x02bc), 
            chr(0x0625): chr(0x02bc), 
            chr(0x0623): chr(0x02bc), 
            chr(0x0624): chr(0x02bc),
            chr(0x0621): chr(0x02bc),
            chr(0x064E) + chr(0x064E): 'aa', 
            chr(0x0622): chr(0x02bc) + 'aa',
            chr(0x064E) + chr(0x0627): 'aa',
            chr(0x064E) + chr(0x0649): 'aa',
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
            chr(0x0645): 'm',
            chr(0x0646): 'n',
            chr(0x0647): 'h',
            chr(0x0648): 'w',
            chr(0x064A): 'y',
            ' ': ' ',
  }

  a_rules = 'Lrqṣṭġḍḍḫ'
  l_rules = 'uaALLAAh'