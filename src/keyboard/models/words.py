#
import json

#
from django.db import models
from django.contrib import admin

class Word(models.Model):
    current = models.CharField(max_length=20, null=True)
    next = models.CharField(max_length=20, null=True)
    es_current = models.CharField(max_length=20, null=True)
    es_next = models.CharField(max_length=20, null=True)

    def __str__(self):
        return "{} {} | {} {}".format(self.current, self.next, self.es_current, self.es_next)


@admin.register(Word)
class ViewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "current",
        "next",
        "es_current",
        "es_next",
    )
    search_fields = ['next', 'current', 'es_current', 'es_next']
    