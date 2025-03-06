"""
keyboard:
we have 2 types of writing:
  - Phonemic typing: typing the sound and its length, ready for synthesis sound
  - easy shrift: no dots and no diacritics
  
  
Phonemic typing:
we type sound as a sequence of syllables with:
  - length 1 (cv)        = 2*avll
  - length 2 (cvvv, cvcc)    = 4*avll
we have 2 dictionaries:
  - Language dictionary: we have a full book split in sentences, of various length, 
    with full dots and diacritics, ready for synthesis.
  - the same dictionary is also turned into 'easy shrift', stripped of dots and diacritics 
    is saved in this dictionary. as u write in easy shrift, 
    the dictionary adds dots and diacritics. If new ready for synthesis text is typed, 
    it is added to Language dictionary and a stripped version is added to the easy shrift 
    dictionary.
  - their is the option of saving specific type of text, based on rhythm, or based on vocabulary.
  
as the user types, the keyboard will tell them the sequence of their text. 
The dictionary can recognize 16 different rhythms. It saves anything in those 16 rhythms 
as "Poetry".

As letters r typed, syllables r suggested, and syllables r selcted, 
new syllables r suggested only if it follows the 16 rhythms. 
If it does not follow the rhythms, it is Not Poetry, nothing saved, nothing suggested.

as a syllable is selected from suggestions, the cursor is placed in a specific spot 
of that syllable, a 'space' is suggested in that spot, 
if a space is inserted, its a juncture between 2 words, 
new letters may be created there. (mad >> ma ald). 
when a word is typed, another word is suggested, or another syllable.

the 16 rhythms r: (name, rhythm )
  - ()



الطويل
1221222 1221222

المديد
21222122122 21222122122 

البسيط
22122122212121

الوافر
1211212112122

الكامل
112121121211212

الهزج
12221222

الرجز
221222122212

الرملن
212221222122

السريع
22122212212

المنسرح
221222212112

الخفيف
212222122122

المضارع
12212122

المقتضب
21222122

المجتث
22122122

المتقارب
12212212212

المتدارك
121121121121


split sentence into cvcc, cvvv, or cv

add rhythm table
add sentence table
table phonemics
table easy shrift
"""