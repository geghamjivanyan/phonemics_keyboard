#
import json
from typing import Dict, Any
from django.db import models
from django.contrib import admin
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Alphabet(models.Model):
    """
    Model representing a mapping between Arabic and transliterated characters.
    
    This model stores mappings between Arabic characters and their
    transliterated forms, used for text conversion.
    """
    
    arabic = models.CharField(
        _('arabic character'),
        max_length=5,
        null=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(5)
        ],
        db_index=True,
        help_text=_('The Arabic character or sequence')
    )
    
    translit = models.CharField(
        _('transliterated character'),
        max_length=5,
        null=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(5)
        ],
        db_index=True,
        help_text=_('The transliterated form of the character')
    )

    class Meta:
        """Meta options for the Alphabet model."""
        verbose_name = _('alphabet mapping')
        verbose_name_plural = _('alphabet mappings')
        indexes = [
            models.Index(fields=['arabic']),
            models.Index(fields=['translit'])
        ]
        ordering = ['arabic']
        constraints = [
            models.UniqueConstraint(
                fields=['arabic', 'translit'],
                name='unique_alphabet_mapping'
            )
        ]

    def __str__(self) -> str:
        """Return a string representation of the alphabet mapping."""
        return f"{self.arabic} → {self.translit}"

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the alphabet mapping to a dictionary.
        
        Returns:
            Dict containing arabic and translit characters
        """
        return {
            "arabic": self.arabic,
            "translit": self.translit,
        }

    def clean(self) -> None:
        """
        Validate the model data.
        
        Ensures that both arabic and translit fields are set.
        """
        super().clean()
        
        if not self.arabic:
            raise models.ValidationError({
                'arabic': _('Arabic character is required')
            })
            
        if not self.translit:
            raise models.ValidationError({
                'translit': _('Transliterated character is required')
            })

    def save(self, *args, **kwargs) -> None:
        """Save the model instance after validation."""
        self.full_clean()
        super().save(*args, **kwargs)


@admin.register(Alphabet)
class AlphabetAdmin(admin.ModelAdmin):
    """Admin interface configuration for the Alphabet model."""
    
    list_display = (
        'id',
        'arabic',
        'translit'
    )
    
    search_fields = [
        'arabic',
        'translit'
    ]
    
    list_filter = (
        'arabic',
        'translit'
    )
    
    ordering = ('arabic',)
    
    def get_queryset(self, request):
        """Return a queryset with optimized database queries."""
        return super().get_queryset(request).select_related()


