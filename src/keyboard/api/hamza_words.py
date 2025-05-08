#
import json

#
from django.views.generic import View
from django.http import HttpResponse
from django.db.models.functions import Right

from ..models.koran import Koran
from ..models.hamza_words import HamzaWord

from ..tools.utils import is_vowel, sort_by_frequency
from ..tools.constants import Diacritics as D
from ..tools.transformation_tools import from_arabic_to_translit, from_translit_to_arabic 
from ..tools.transformation_tools import classify, split


class HamzaWordView(View):

    def get(self, request):

        hamzas = [chr(0x0625), chr(0x0624), chr(0x0623), chr(0x0626), chr(0x0621)]

        blocks = Koran.objects.all()
    
        for block in blocks:
            words = block.arabic.split(' ')
            for word in words:
                if any(letter in word for letter in hamzas):
                    easy_shrift = HamzaWordView.remove_dots(word)
                    hamza = easy_shrift
                    for h in hamzas:
                        hamza = hamza.replace(h, chr(0x0621))
                
                    HamzaWord.objects.get_or_create(
                        phonemic=word, 
                        easy_shrift=easy_shrift,
                        hamza=hamza
                    )
                
        return HttpResponse(
            status=200,
            content_type="application/json; charset=utf-8",
        )

    @staticmethod
    def remove_dots(text):

        text = text.encode('utf-8')
        
        for d in D.diacritics:
            text = text.replace(d, b'')
            
        for k, v in D.dotless.items():
            text = text.replace(k, v)
            
        return text.decode('utf-8')

    @staticmethod
    def remove(request):
        objs = HamzaWord.objects.all()
        for obj in objs:
            obj.delete()

        return HttpResponse(
            status=200,
            content_type="application/json; charset=utf-8",
        )
