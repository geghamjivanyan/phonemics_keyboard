#
import json

#
from django.db import models
from django.contrib import admin

class TranslitWord(models.Model):
    prev = models.CharField(max_length=5, null=True, blank=True)
    current = models.CharField(max_length=5, null=True, blank=True)
    next = models.CharField(max_length=5, null=True, blank=True)
    pattern = models.CharField(max_length=3, null=True, blank=True)

@admin.register(TranslitWord)
class TranslitViewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "prev",
        "current",
        "next",
        "pattern",
    )