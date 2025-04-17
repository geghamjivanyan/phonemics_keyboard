#
import json

#
from django.db import models
from django.contrib import admin

# Create your models here.

class TranslitKoran(models.Model):
    chapter = models.CharField(max_length=3, null=True)
    block = models.CharField(max_length=3, null=True)
    text = models.CharField(max_length=500, null=True)
    cut_text = models.CharField(max_length=500, null=True, blank=True)
    pattern = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return str(
            json.dumps(
                {
                    "chapter": self.chapter,
                    "block": self.block,
                    "text": self.text,
                }
            )
        )

    def to_dict(self):
        return {
            "chapter": self.chapter, 
            "block": self.block,
            "text": self.text,
        }


@admin.register(TranslitKoran)
class TranslitKoranAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "chapter",
        "block",
        "text",
        "cut_text",
        "pattern",
    )


