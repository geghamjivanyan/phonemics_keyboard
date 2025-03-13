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

from ..models.translit_koran import TranslitKoran

#
def is_vowel(letter):
    """
    check if letter is vowel

    :params letter - letter which should be checked

    :returns: True or False
    """
    vowels = 'aiuAYNW*'
    return letter in vowels

class TranslitKoranView(View):
    
    def get(self, request):
        filename = "{}/keyboard/api/koran_text.txt".format(settings.BASE_DIR)

        with open(filename) as f:
            lines = f.readlines()
            i = 0
            for line in lines:
                if i % 100 == 0:
                    print("I", i)
                line = line.strip()
                if len(line):
                    cb = line.split(' ')[0].split('.')
                    chapter = f'{int(cb[0]):03d}'
                    block = cb[2]
                    line = line.replace('*', '')
                    text = line.split(' ')[1]
                    if text[0] == '.':
                        text = text[1:]
                    if text[-1] == '.':
                        text = text[:-1]
                    cut_text = TranslitKoranView.limit_consecutive_letters(text)
                    pattern = TranslitKoranView.classify(cut_text)
                    TranslitKoran(
                        chapter=chapter, 
                        block=block, 
                        text=text, 
                        cut_text=cut_text,
                        pattern=pattern
                    ).save()
                i += 1

        return HttpResponse(
            status=200,
            content_type="application/json; charset=utf-8",
        )

    @staticmethod
    def split(request):
        blocks = TranslitKoran.objects.all()

        for block in blocks[:10]:
            text = block.text.replace('.', '')
            res = TranslitKoranView.limit_consecutive_letters(text)
            block.text = text
            block.cut_text = res
            block.pattern = TranslitKoranView.classify(res)

            block.save()

        return HttpResponse(
            status=200,
            content_type="application/json; charset=utf-8",
        )     
    
    @staticmethod
    def limit_consecutive_letters(text):
        # Replace any letter appearing more than twice consecutively with only two occurrences
        res =  re.sub(r'(.)\1{2,}', r'\1\1', text)
        print("RES", res)
        res = res.replace('N', '').replace('W', '').replace('Y','')
        print("RES 2", res)
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

        s = s.strip()

        if len(s) >= 4 and TranslitKoranView.is_cvvc(s[-4:]):
            s = s[:-1] + ' ' + s[-1]
        
        return s
    
    @staticmethod
    def is_cvvc(text):

        return not is_vowel(text[0]) and is_vowel(text[1]) and \
            is_vowel(text[2]) and not is_vowel(text[3])

    @staticmethod
    def classify(text):
        parts = text.split(' ')
        pattern = ''
        for part in parts:
            if len(part) <= 2:
                pattern += '1'
            elif len(part) == 3:
                pattern += '2'
            else:
                pattern += '3'
        return pattern
    
    @staticmethod
    def remove(request):
        blocks = TranslitKoran.objects.all()

        i = 0
        for block in blocks:
            if i % 100 == 0:
                print("I", i)
            i += 1    
            block.delete()

        return HttpResponse(
            status=200,
            content_type="application/json; charset=utf-8",
        )
    
    @staticmethod
    def remove(request):
        objs = TranslitKoran.objects.all()
        for obj in objs:
            obj.delete()