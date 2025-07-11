#
import json
from typing import List, Optional, Dict, Any

#
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.db.models.functions import Right
from django.core.exceptions import ValidationError
from django.db import transaction

from ..models.words import Word
from ..models.koran import Koran
from ..models.translit_words import TranslitWord
from ..models.rhythms import Rhythm
from ..models.hamza_words import HamzaWord

from ..tools.utils import is_vowel, sort_by_frequency, is_keyboard_changed
from ..tools.utils import change_hamza, change_text
from ..tools.constants import Diacritics as D
from ..tools.transformation_tools import from_arabic_to_translit, from_translit_to_arabic 
from ..tools.transformation_tools import classify, split, apply_transformation_rules

from .hamza_words import HamzaWordView

class StatisticView(View):
    """View for handling word-related operations."""

    def get(self, request) -> HttpResponse:
        """
        Get words from Koran blocks.
        
        Args:
            request: HTTP request object containing count parameter
            
        Returns:
            HttpResponse with status 200 if successful
        """
        try:
            words = Word.objects.all()

            uniques = set()

            for word in words:
                uniques.add(word.current)

            print("Unique words in Koran ", len(uniques))
                    
            return HttpResponse(
                status=200,
                content_type="application/json; charset=utf-8",
            )
        except (ValueError, ValidationError) as e:
            return JsonResponse(
                {"error": str(e)},
                status=400
            )
        except Exception as e:
            return JsonResponse(
                {"error": "Internal server error"},
                status=500
            )

    