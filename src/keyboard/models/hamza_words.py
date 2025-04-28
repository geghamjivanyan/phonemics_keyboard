#
import json

#
from django.db import models
from django.contrib import admin

class HamzaWord(models.Model):
    phonemic = models.CharField(max_length=20, null=True)
    easy_shrift = models.CharField(max_length=20, null=True)
    hamza = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return "{} {} | {} {}".format(self.phonemic, self.easy_shrift, self.hamza)


@admin.register(HamzaWord)
class HamzaWordAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "phonemic",
        "easy_shrift",
        "hamza",
    )
    search_fields = ['phonemic', 'easy_shrift', 'hamza']
    