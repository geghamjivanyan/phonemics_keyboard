#
import json
from typing import Optional

#
from django.db import models
from django.contrib import admin
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.translation import gettext_lazy as _

class Word(models.Model):
    """
    Model representing a word and its next word in sequence.
    
    This model stores Arabic words and their transliterated forms (easy shrift).
    Each word can have a next word in sequence, and both can have their
    transliterated forms.
    """
    
    current = models.CharField(
        _('current word'),
        max_length=20,
        null=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(20)
        ],
        db_index=True,
        help_text=_('The current Arabic word')
    )
    
    next = models.CharField(
        _('next word'),
        max_length=20,
        null=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(20)
        ],
        db_index=True,
        help_text=_('The next Arabic word in sequence')
    )
    
    es_current = models.CharField(
        _('easy shrift current'),
        max_length=20,
        null=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(20)
        ],
        help_text=_('The transliterated form of the current word')
    )
    
    es_next = models.CharField(
        _('easy shrift next'),
        max_length=20,
        null=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(20)
        ],
        help_text=_('The transliterated form of the next word')
    )

    class Meta:
        """Meta options for the Word model."""
        verbose_name = _('word')
        verbose_name_plural = _('words')
        indexes = [
            models.Index(fields=['current', 'next']),
            models.Index(fields=['es_current', 'es_next'])
        ]
        ordering = ['current']

    def __str__(self) -> str:
        """Return a string representation of the word pair."""
        return f"{self.current} {self.next} | {self.es_current} {self.es_next}"

    def clean(self) -> None:
        """
        Validate the model data.
        
        Ensures that if current is set, es_current must also be set.
        Similarly, if next is set, es_next must also be set.
        """
        super().clean()
        
        if self.current and not self.es_current:
            raise models.ValidationError({
                'es_current': _('Easy shrift current is required when current word is set')
            })
            
        if self.next and not self.es_next:
            raise models.ValidationError({
                'es_next': _('Easy shrift next is required when next word is set')
            })

    def save(self, *args, **kwargs) -> None:
        """Save the model instance after validation."""
        self.full_clean()
        super().save(*args, **kwargs)


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    """Admin interface configuration for the Word model."""
    
    list_display = (
        'id',
        'current',
        'next',
        'es_current',
        'es_next',
    )
    
    search_fields = [
        'current',
        'next',
        'es_current',
        'es_next'
    ]
    
    list_filter = (
        'current',
        'next'
    )
    
    ordering = ('current', 'next')
    
    def get_queryset(self, request):
        """Return a queryset with optimized database queries."""
        return super().get_queryset(request).select_related()
    