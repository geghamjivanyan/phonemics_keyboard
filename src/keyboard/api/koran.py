#
import re
import json
import requests

#
from datetime import datetime
from bs4 import BeautifulSoup

#
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

from ..models.koran import Koran


class KoranView(View):
    def get(self, request):

        res = requests.get("https://ar.wikisource.org/wiki/%D8%A7%D9%84%D9%82%D8%B1%D8%A2%D9%86_%D8%A7%D9%84%D9%83%D8%B1%D9%8A%D9%85_(%D8%A8%D8%A7%D9%84%D8%B1%D8%B3%D9%85_%D8%A7%D9%84%D8%A5%D9%85%D9%84%D8%A7%D8%A6%D9%8A)/%D8%A7%D9%84%D9%86%D8%B5_%D8%A7%D9%84%D9%85%D8%B4%D9%83%D9%88%D9%84")

        soup = BeautifulSoup(res.text, features="html.parser")

        chapters = soup.find_all('div', class_='mw-heading mw-heading2')

        pattern = r'\(\d+\)'

        for i in range(len(chapters)):
            chapter = chapters[i].nextSibling.nextSibling.nextSibling

            blocks = re.split(pattern, chapter.text)

            for j in range(len(blocks) - 1):
                text = self._manage_text(blocks[j])

                Koran(chapter=f"{i+1:03d}", block=f"{j+1:03d}", arabic=text).save()

        return HttpResponse(
            status=200,
            content_type="application/json; charset=utf-8",
        )
    
    def _manage_text(self, text):

        text = text.strip().replace(chr(0x0652).encode('utf-8').decode('utf-8'), '')
        diacritics = [
            chr(0x0650).encode('utf-8').decode('utf-8'), 
            chr(0x064F).encode('utf-8').decode('utf-8'), 
            chr(0x064E).encode('utf-8').decode('utf-8')
        ]
        if text[-1] in diacritics:
            text = text[:-1]

        return text

    @staticmethod
    def remove_all(request):
        texts = Koran.objects.all()
        for text in texts:
            text.delete()

        return HttpResponse("OK")

    @staticmethod
    def easy_shrift(request):

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

        blocks = Koran.objects.all()
        i = 0
        for block in blocks:
            text = block.arabic.encode('utf-8')
            #print("BEFORE", len(block.arabic), "\n", block.arabic)
            if i % 100 == 0:
                print("I", i)
            i+=1
            for d in diacritics:
                #print("d", d)
                text = text.replace(d, b'')
                #print("TEXT\n", text.decode('utf-8'))
            for k, v in dotless.items():
                #print("k", k, "v", v)
                text = text.replace(k, v)
            #print("AFTER", len(text.decode('utf-8')), "\n", text.decode('utf-8'))
            block.easy_shrift = text.decode('utf-8')
            block.save()

        return HttpResponse("OK")
    
    @staticmethod
    def remove(request):
        objs = Koran.objects.all()
        for obj in objs:
            obj.delete()