#
import json

#
from django.db import models
from django.contrib import admin

class Word(models.Model):
    prev = models.CharField(max_length=20, null=True)
    current = models.CharField(max_length=20, null=True)
    next = models.CharField(max_length=20, null=True)


@admin.register(Word)
class ViewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "prev",
        "current",
        "next"
    )