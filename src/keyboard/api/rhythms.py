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

from ..models.rhythms import Rhythm
from ..tools.constants import Rhythm as R

class RhythmView(View):
    def get(self, request):

        for k, v in R.rhythms.items():
            r = Rhythm(name=v, pattern=k)
            r.save()

        return HttpResponse(
            status=200,
            content_type="application/json; charset=utf-8",
        )



