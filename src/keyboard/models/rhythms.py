#
import json

#
from django.db import models
from django.contrib import admin

# Create your models here.

class Rhythm(models.Model):
    name = models.CharField(max_length=50, null=True)
    pattern = models.CharField(max_length=50, null=True)


    def __str__(self):
        return str(
            json.dumps(
                {
                    "name": self.name,
                    "pattern": self.pattern,
                }
            )
        )

    def to_dict(self):
        return {
            "name": self.name, 
            "pattern": self.pattern,
        }


@admin.register(Rhythm)
class RhythmAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "pattern",
    )


