#
import json
from typing import Dict, Any
from django.db import models
from django.contrib import admin
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Rhythm(models.Model):
    """
    Model representing a rhythm pattern in Arabic poetry.
    
    This model stores rhythm patterns used in Arabic poetry, where each pattern
    is represented by a sequence of numbers indicating the syllable structure.
    """
    
    name = models.CharField(
        _('rhythm name'),
        max_length=50,
        null=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(50)
        ],
        db_index=True,
        help_text=_('The name of the rhythm pattern')
    )
    
    pattern = models.CharField(
        _('rhythm pattern'),
        max_length=50,
        null=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(50),
            RegexValidator(
                regex=r'^[0-9]+$',
                message=_('Pattern must contain only numbers')
            )
        ],
        db_index=True,
        help_text=_('The numerical pattern representing the rhythm structure')
    )

    class Meta:
        """Meta options for the Rhythm model."""
        verbose_name = _('rhythm')
        verbose_name_plural = _('rhythms')
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['pattern'])
        ]
        ordering = ['name']
        constraints = [
            models.UniqueConstraint(
                fields=['name'],
                name='unique_rhythm_name'
            )
        ]

    def __str__(self) -> str:
        """Return a string representation of the rhythm."""
        return f"{self.name} ({self.pattern})"

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the rhythm instance to a dictionary.
        
        Returns:
            Dict containing rhythm name and pattern
        """
        return {
            "name": self.name,
            "pattern": self.pattern,
        }

    def clean(self) -> None:
        """
        Validate the model data.
        
        Ensures that both name and pattern are set and valid.
        """
        super().clean()
        
        if not self.name:
            raise models.ValidationError({
                'name': _('Rhythm name is required')
            })
            
        if not self.pattern:
            raise models.ValidationError({
                'pattern': _('Rhythm pattern is required')
            })

    def save(self, *args, **kwargs) -> None:
        """Save the model instance after validation."""
        self.full_clean()
        super().save(*args, **kwargs)


@admin.register(Rhythm)
class RhythmAdmin(admin.ModelAdmin):
    """Admin interface configuration for the Rhythm model."""
    
    list_display = (
        'id',
        'name',
        'pattern',
    )
    
    search_fields = [
        'name',
        'pattern'
    ]
    
    list_filter = (
        'name',
    )
    
    ordering = ('name',)
    
    def get_queryset(self, request):
        """Return a queryset with optimized database queries."""
        return super().get_queryset(request).select_related()


