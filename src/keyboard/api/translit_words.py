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

from ..models.translit_words import TranslitWord
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



class TranslitWordView(View):

    def get(self, request):
        count = int(request.GET.get("count", None))
        blocks = TranslitKoran.objects.filter(id__gt=count*600, id__lt=(count+1)*600-1)
        i = 0
        for block in blocks:
            if i % 100 == 0:
                print("I", i)
            i+=1
            words = block.cut_text.split(' ')

            if len(words) == 2:
                pattern="{}{}".format(
                    self.classify(words[0]), 
                    self.classify(words[1])
                )
                TranslitWord.objects.get_or_create(
                    prev=words[0], 
                    current=words[1], 
                    pattern=pattern)
            elif len(words) == 1:
                TranslitWord.objects.get_or_create(prev=words[0], pattern=self.classify(words[0]))
            else:
                pattern="{}{}{}".format(
                    self.classify(words[0]), 
                    self.classify(words[1]),
                    self.classify(words[2])
                )
                TranslitWord.objects.get_or_create(
                    prev=words[0], 
                    current=words[1], 
                    next=words[2],
                    pattern=pattern
                )
                for i in range(2, len(words)-1, 1):
                    #print("I", i, i+1, len(words))
                    next=words[i+1]
                    #print("words", words[i+1])
                    prev= words[i-1]
                    current = words[i]
                    pattern="{}{}{}".format(
                        self.classify(prev), 
                        self.classify(current),
                        self.classify(next)
                    )
                    TranslitWord.objects.get_or_create(
                        prev=prev, 
                        current=current, 
                        next=next,
                        pattern=pattern,
                    )

                pattern="{}{}".format(
                    self.classify(words[-2]), 
                    self.classify(words[-1])
                )
                TranslitWord.objects.get_or_create(
                    prev=words[-2], 
                    current=words[-1], 
                    pattern=pattern
                )
            
        return HttpResponse(
            status=200,
            content_type="application/json; charset=utf-8",
        )

    @staticmethod
    def search(request):
        words = 'رَبِّ'
        words = words.split(' ')
        print("WORDS", len(words))
        data = []
        if len(words) == 1:
            print("IIIF", words[0])
            result = TranslitWord.objects.filter(prev=words[0])
            print("RESULT", result)
            for r in result:
                data.append(r.current)
        if len(words) == 2:
            result = TranslitWord.objects.filter(prev=words[0], current=words[1])
            if len(result):
                for r in result:
                    data.append(r.next)
            else:
                result = TranslitWord.objects.filter(prev=words[1])
                for r in result:
                    data.append(r.current)

        return HttpResponse(
            json.dumps({"data": data}),
            status=200,
            content_type="application/json; charset=utf-8",
        )

    @staticmethod
    def classify(text):
        if len(text) <= 2:
            return '1'
        elif len(text) == 3:
            return '2'
        return '3'        

    
    @staticmethod
    def remove(request):
        objs = TranslitWord.objects.all()
        for obj in objs:
            obj.delete()

        return HttpResponse("OK")

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
    def suggest(request):

        text = ''
        data = []
        if text[-1] != ' ':
            syl = TranslitWordView.split(text)
            cut = syl.split(' ')
            if len(cut) == 1:
                suggestions = TranslitWord.objects.filter(prev=cut[0])
                for suggest in suggestions:
                    if suggest.current:
                        data.append(suggest.current)
            if len(cut) > 1:
                suggestions = TranslitWord.objects.filter(prev=cut[-2], current=cut[-1])
                for suggest in suggestions:
                    if suggest.next:
                        data.append(suggest.next)

        # if it is word we should use easy shrift