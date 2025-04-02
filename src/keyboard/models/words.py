#
import json

#
from django.db import models
from django.contrib import admin

class Word(models.Model):
    prev = models.CharField(max_length=20, null=True)
    current = models.CharField(max_length=20, null=True)
    next = models.CharField(max_length=20, null=True)

    def __str__(self):
        return "{} {} {}".format(self.prev, self.current, self.next)


@admin.register(Word)
class ViewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "prev",
        "current",
        "next"
    )
    