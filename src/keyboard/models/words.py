#
import json

#
from django.db import models
from django.contrib import admin

class Word(models.Model):
    current = models.CharField(max_length=20, null=True)
    next = models.CharField(max_length=20, null=True)

    def __str__(self):
        return "{} {}".format(self.current, self.next)


@admin.register(Word)
class ViewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "current",
        "next"
    )
    search_fields = ['next', 'current']
    