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


class RhythmView(View):
    def get(self, request):

        rhythms = Rhythm.objects.all()

        data = [r.to_dict() for r in rhythms]
        print("SETTINGS", settings.DATA_UPLOAD_MAX_NUMBER_FIELDS)
        return HttpResponse(
            json.dumps({"data": data}),
            status=200,
            content_type="application/json; charset=utf-8",
        )



