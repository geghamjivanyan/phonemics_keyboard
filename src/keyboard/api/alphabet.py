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

from ..models.alphabet import Alphabet

class AlphabetView(View):

    def get(self, request):
        """
            • aa   >  064E + 0627
            • AA > 064E + 0627
            • ii       >     0650 + 064A
            • uu    >     064F + 0648
            • A  >  064E
            • a  >  064E
            • i        >     0650
            • u       >     064F
            • ʼ         >     0621
            • ʻ         >     0639
            • b       >     0628
            • t        >     062A
            • d      >     062F
            • ǧ      >     062C
            • r       >     0631
            • ṯ       >     062B
            • z       >      0632
            • s       >      0633
            • ḥ      >     062D
            • ḫ      >     062E
            • ḏ      >     0630
            • ṣ      >     0635
            • š       >      0634
            • ḍ       >      0636
            • ẓ      >      0638
            • ṭ       >     0637
            • ġ      >     063A
            • f        >      0641
            • q       >      0642
            • k       >      0643
            • l        >      0644
            • m     >      0645
            • n      >      0646
            • h      >      0647
            • w     >      0648
            • y      >      064A
        """