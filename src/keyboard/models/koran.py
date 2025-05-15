from typing import Dict, Any
import json
from django.db import models
from django.contrib import admin
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.utils.translation import gettext_lazy as _

class Koran(models.Model):
    """
    Model representing a block of text from the Quran.
    
    This model stores blocks of text from the Quran, including:
    - chapter: The chapter number
    - block: The block number within the chapter
    - arabic: The Arabic text
    - easy_shrift: The simplified transliterated text
    """
    
    chapter = models.CharField(
        _('chapter number'),
        max_length=3,
        null=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(3),
            RegexValidator(
                regex=r'^[0-9]+$',
                message=_('Chapter must contain only numbers')
            )
        ],
        db_index=True,
        help_text=_('The chapter number in the Quran')
    )
    
    block = models.CharField(
        _('block number'),
        max_length=3,
        null=True,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(3),
            RegexValidator(
                regex=r'^[0-9]+$',
                message=_('Block must contain only numbers')
            )
        ],
        db_index=True,
        help_text=_('The block number within the chapter')
    )
    
    arabic = models.TextField(
        _('arabic text'),
        null=True,
        validators=[
            MinLengthValidator(1)
        ],
        help_text=_('The Arabic text of the block')
    )
    
    easy_shrift = models.TextField(
        _('easy shrift text'),
        null=True,
        validators=[
            MinLengthValidator(1)
        ],
        help_text=_('The simplified transliterated text')
    )

    class Meta:
        """Meta options for the Koran model."""
        verbose_name = _('quran block')
        verbose_name_plural = _('quran blocks')
        indexes = [
            models.Index(fields=['chapter']),
            models.Index(fields=['block']),
            models.Index(fields=['chapter', 'block'])
        ]
        ordering = ['chapter', 'block']
        constraints = [
            models.UniqueConstraint(
                fields=['chapter', 'block'],
                name='unique_quran_block'
            )
        ]

    def __str__(self) -> str:
        """Return a string representation of the Quran block."""
        return f"Chapter {self.chapter}, Block {self.block}"

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the Quran block to a dictionary.
        
        Returns:
            Dict containing chapter, block, arabic text, and easy shrift
        """
        return {
            "chapter": self.chapter,
            "block": self.block,
            "arabic": self.arabic,
            "easy_shrift": self.easy_shrift,
        }

    def clean(self) -> None:
        """
        Validate the model data.
        
        Ensures that all required fields are set and valid.
        """
        super().clean()
        
        if not self.chapter:
            raise models.ValidationError({
                'chapter': _('Chapter number is required')
            })
            
        if not self.block:
            raise models.ValidationError({
                'block': _('Block number is required')
            })
            
        if not self.arabic:
            raise models.ValidationError({
                'arabic': _('Arabic text is required')
            })
            
        if not self.easy_shrift:
            raise models.ValidationError({
                'easy_shrift': _('Easy shrift text is required')
            })

    def save(self, *args, **kwargs) -> None:
        """Save the model instance after validation."""
        self.full_clean()
        super().save(*args, **kwargs)


@admin.register(Koran)
class KoranAdmin(admin.ModelAdmin):
    """Admin interface configuration for the Koran model."""
    
    list_display = (
        'id',
        'chapter',
        'block',
        'arabic',
        'easy_shrift'
    )
    
    search_fields = [
        'chapter',
        'block',
        'arabic',
        'easy_shrift'
    ]
    
    list_filter = (
        'chapter',
        'block'
    )
    
    ordering = ('chapter', 'block')
    
    def get_queryset(self, request):
        """Return a queryset with optimized database queries."""
        return super().get_queryset(request).select_related()


