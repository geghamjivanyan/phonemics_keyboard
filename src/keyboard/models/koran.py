#
import json

#
from django.db import models
from django.contrib import admin

# Create your models here.

class Koran(models.Model):
    chapter = models.CharField(max_length=3, null=True)
    block = models.CharField(max_length=3, null=True)
    arabic = models.TextField(null=True)
    easy_shrift = models.TextField(null=True)

    def __str__(self):
        return str(
            json.dumps(
                {
                    "chapter": self.chapter,
                    "block": self.block,
                    "arabic": self.arabic,
                    "easy_shrift": self.easy_shrift,
                }
            )
        )

    def to_dict(self):
        return {
            "chapter": self.chapter, 
            "block": self.block,
            "arabic": self.arabic,
            "easy_shrift": self.easy_shrift,
        }


@admin.register(Koran)
class KoranAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "chapter",
        "block",
        "arabic",
        "easy_shrift"
    )


