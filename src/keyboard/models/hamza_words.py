#
import json
from typing import Optional

#
from django.db import models
from django.contrib import admin
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.translation import gettext_lazy as _

class HamzaWord(models.Model):
    """
    Model representing a word with hamza variations.
    
    This model stores different forms of words containing hamza:
    - phonemic: The standard form
    - easy_shrift: The simplified form
    - hamza: The form with hamza
    """
    
    phonemic = models.CharField(
        _('phonemic form'),
        max_length=20,
        null=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(20)
        ],
        db_index=True,
        help_text=_('The standard phonemic form of the word')
    )
    
    easy_shrift = models.CharField(
        _('easy shrift form'),
        max_length=20,
        null=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(20)
        ],
        db_index=True,
        help_text=_('The simplified form of the word')
    )
    
    hamza = models.CharField(
        _('hamza form'),
        max_length=20,
        null=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(20)
        ],
        db_index=True,
        help_text=_('The form of the word with hamza')
    )

    class Meta:
        """Meta options for the HamzaWord model."""
        verbose_name = _('hamza word')
        verbose_name_plural = _('hamza words')
        indexes = [
            models.Index(fields=['phonemic']),
            models.Index(fields=['easy_shrift']),
            models.Index(fields=['hamza'])
        ]
        ordering = ['phonemic']
        constraints = [
            models.UniqueConstraint(
                fields=['phonemic', 'easy_shrift', 'hamza'],
                name='unique_hamza_word'
            )
        ]

    def __str__(self) -> str:
        """Return a string representation of the hamza word."""
        return f"{self.phonemic} {self.easy_shrift} | {self.hamza}"

    def clean(self) -> None:
        """
        Validate the model data.
        
        Ensures that at least one form of the word is provided.
        """
        super().clean()
        
        if not any([self.phonemic, self.easy_shrift, self.hamza]):
            raise models.ValidationError(
                _('At least one form of the word must be provided')
            )

    def save(self, *args, **kwargs) -> None:
        """Save the model instance after validation."""
        self.full_clean()
        super().save(*args, **kwargs)


@admin.register(HamzaWord)
class HamzaWordAdmin(admin.ModelAdmin):
    """Admin interface configuration for the HamzaWord model."""
    
    list_display = (
        'id',
        'phonemic',
        'easy_shrift',
        'hamza',
    )
    
    search_fields = [
        'phonemic',
        'easy_shrift',
        'hamza'
    ]
    
    list_filter = (
        'phonemic',
        'easy_shrift',
        'hamza'
    )
    
    ordering = ('phonemic',)
    
    def get_queryset(self, request):
        """Return a queryset with optimized database queries."""
        return super().get_queryset(request).select_related()
    