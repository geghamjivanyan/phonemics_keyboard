
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
