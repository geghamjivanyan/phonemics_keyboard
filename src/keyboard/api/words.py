#
import json

#
from datetime import datetime

#
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

from ..models.words import Word
from ..models.koran import Koran


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
    def search(request):
        words = 'رَبِّ'
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

        return HttpResponse(
            json.dumps({"data": data}),
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

    """
    062E + . = 062C   (خ ج)
    066E + . = 0628   (ب)
    0628 + . = 062A  (ب ت)
    0646 + . = 062A  (ن  ت)
    0647 + . = 0629   (ه  ة)
    064E + . = 064B   (فتح   )
    064F + . = 064C  (ضم   )
    0650 + . = 064D  (كسر   )
    0631 + . = 0632   (ر  ز)
    062F + . = 0630   (د ذ)
    062A + . = 062B   (ت ث)
    0637 + . = 0638   (ط ظ)
    0633 + . = 0634   (س ش
    0635
    """