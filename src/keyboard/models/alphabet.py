#
import json

#
from django.db import models
from django.contrib import admin

# Create your models here.

class Alphabet(models.Model):
    arabic = models.CharField(max_length=5, null=True)
    translit = models.CharField(max_length=5, null=True)

    def __str__(self):
        return str(
            json.dumps(
                {
                    "arabic": self.arabic,
                    "translit": self.translit,
                }
            )
        )

    def to_dict(self):
        return {
            "arabic": self.arabic,
            "translit": self.translit,
        }


@admin.register(Alphabet)
class AlphabetAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "arabic",
        "translit"
    )


