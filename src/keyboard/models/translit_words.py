#
import json
from typing import Optional

#
from django.db import models
from django.contrib import admin
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.translation import gettext_lazy as _

class TranslitWord(models.Model):
    """
    Model representing a transliterated word sequence.
    
    This model stores transliterated words in sequence, where each word
    can have a previous and next word, along with its pattern.
    """
    
    prev = models.CharField(
        _('previous word'),
        max_length=5,
        null=True,
        blank=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(5)
        ],
        db_index=True,
        help_text=_('The previous word in sequence')
    )
    
    current = models.CharField(
        _('current word'),
        max_length=5,
        null=True,
        blank=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(5)
        ],
        db_index=True,
        help_text=_('The current word')
    )
    
    next = models.CharField(
        _('next word'),
        max_length=5,
        null=True,
        blank=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(5)
        ],
        db_index=True,
        help_text=_('The next word in sequence')
    )
    
    pattern = models.CharField(
        _('word pattern'),
        max_length=3,
        null=True,
        blank=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(3)
        ],
        help_text=_('The pattern of the word')
    )

    class Meta:
        """Meta options for the TranslitWord model."""
        verbose_name = _('transliterated word')
        verbose_name_plural = _('transliterated words')
        indexes = [
            models.Index(fields=['prev', 'current']),
            models.Index(fields=['current', 'next']),
            models.Index(fields=['pattern'])
        ]
        ordering = ['current']
        constraints = [
            models.UniqueConstraint(
                fields=['prev', 'current', 'next'],
                name='unique_translit_word'
            )
        ]

    def __str__(self) -> str:
        """Return a string representation of the transliterated word sequence."""
        return f"{self.prev} {self.current} {self.next}"

    def clean(self) -> None:
        """
        Validate the model data.
        
        Ensures that at least one of prev, current, or next is set.
        """
        super().clean()
        
        if not any([self.prev, self.current, self.next]):
            raise models.ValidationError(
                _('At least one word in the sequence must be provided')
            )

    def save(self, *args, **kwargs) -> None:
        """Save the model instance after validation."""
        self.full_clean()
        super().save(*args, **kwargs)


@admin.register(TranslitWord)
class TranslitWordAdmin(admin.ModelAdmin):
    """Admin interface configuration for the TranslitWord model."""
    
    list_display = (
        'id',
        'prev',
        'current',
        'next',
        'pattern',
    )
    
    search_fields = [
        'prev',
        'current',
        'next',
        'pattern'
    ]
    
    list_filter = (
        'pattern',
    )
    
    ordering = ('current',)
    
    def get_queryset(self, request):
        """Return a queryset with optimized database queries."""
        return super().get_queryset(request).select_related()