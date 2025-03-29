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

from ..models.words import Word
from ..models.koran import Koran
from ..models.translit_words import TranslitWord

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
            words = block.easy_shrift.split(' ')
            #words = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh']
            if len(words) == 2:
                Word.objects.get_or_create(prev=words[0], current=words[1], next=None)
            elif len(words) == 1:
                Word.objects.get_or_create(prev=words[0], current=None, next=None)
            else:
                Word.objects.get_or_create(prev=words[0], current=words[1], next=words[2])
                for i in range(2, len(words)-1, 1):
                    next=words[i+1]
                    prev= words[i-1]
                    current = words[i]
                    Word.objects.get_or_create(
                        prev=prev, 
                        current=current, 
                        next=next
                    )


                Word.objects.get_or_create(prev=words[-2], current=words[-1], next=None)
            
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

    @staticmethod
    def search(request):
        words = json.loads(request.body).get('text', None)
        print("WORD", words[-1])
        #words = words.replace('_', ' ')
        if words[-1] == "ـ":
            print("AAAAAAAAAAA")
            words = words.split(' ')
            data = []

            if len(words) == 1:
                result = Word.objects.filter(prev=words[0])
                for r in result:
                    data.append(r.current)
            if len(words) == 2:
                result = Word.objects.filter(prev=words[0], current=words[1])
                if len(result):
                    for r in result:
                        data.append(r.next)
                else:
                    result = Word.objects.filter(prev=words[1])
                    for r in result:
                        data.append(r.current)
        else:
            print("TRANSLIT")
            arabic = WordView._from_arabic_to_translit(words)
            if arabic:
                print("ARABIC", arabic)
                cut = WordView.split(arabic)
                print("CUT", cut)

                translits = cut.split(' ')
                print("TRANSLIT", translits)
                data = WordView.suggest(translits)

        data = {
            "rhythms": [],
            "suggestions": data,
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

        translit = {
            chr(0x064E) + chr(0x0627): 'aa',
            chr(0x064E) + chr(0x0627): 'AA',
            chr(0x0650) + chr(0x064A): 'ii',
            chr(0x064F) + chr(0x0648): 'uu',
            chr(0x064E): 'A',
            chr(0x064E): 'a',
            chr(0x0650): 'i',
            chr(0x064F): 'u',
            chr(0x0621): 'ʼ',
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
            chr(0x0644): 'L',
            chr(0x0645): 'm',
            chr(0x0646): 'n',
            chr(0x0647): 'h',
            chr(0x0648): 'w',
            chr(0x064A): 'y',
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
    def split(res):
        s = ''
        i = 0
        while i < len(res)-1:
            if not is_vowel(res[i]) and is_vowel(res[i+1]):
                s += ' ' + res[i:i+2]
                i += 2
            else:
                s += res[i]
                i += 1
        s += res[-1]
        
        return s.strip()
    
    @staticmethod
    def suggest(cut):

        data = []
        if len(cut) == 1:
            suggestions = TranslitWord.objects.filter(prev=cut[0])
            for suggest in suggestions:
                if suggest.current:
                    res = WordView._from_translit_to_arabic(suggest.current)
                    data.append(res)
        if len(cut) > 1:
            suggestions = TranslitWord.objects.filter(prev=cut[-2], current=cut[-1])
            for suggest in suggestions:
                if suggest.next:
                    res = WordView._from_translit_to_arabic(suggest.next)
                    data.append(res)

        return WordView.sort_by_frequency(data)
    
    @staticmethod
    def sort_by_frequency(lst):
        freq = Counter(lst)
        return sorted(set(lst), key=lambda x: freq[x], reverse=True)