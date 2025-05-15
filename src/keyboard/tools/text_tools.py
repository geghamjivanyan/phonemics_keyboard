from typing import List, Optional, Tuple
from dataclasses import dataclass


# Define vowels used in the text processing
VOWELS = 'aiuAYNW*'


def is_vowel(letter: str) -> bool:
    """
    Check if a letter is a vowel.
    
    Args:
        letter: The letter to check
        
    Returns:
        bool: True if the letter is a vowel, False otherwise
        
    Example:
        >>> is_vowel('a')
        True
        >>> is_vowel('b')
        False
    """
    return letter in VOWELS


@dataclass
class SyllablePattern:
    """Represents a syllable pattern in the text."""
    pattern: str
    length: int


class TextManager:
    """
    A class for managing and processing text, particularly for syllable analysis.
    
    This class provides methods for analyzing text patterns and splitting text
    into phonemes based on syllable patterns.
    """
    
    def __init__(self, text: str):
        """
        Initialize the TextManager with input text.
        
        Args:
            text: The text to be processed
        """
        self.text = text

    def _is_cvcc(self, text: str) -> bool:
        """
        Check if text follows a CVCC pattern (consonant-vowel-consonant-consonant).
        
        Args:
            text: Text segment to check
            
        Returns:
            bool: True if text follows CVCC pattern
            
        Example:
            >>> TextManager("")._is_cvcc("bark")
            True
        """
        if len(text) < 4:
            return False
        return (not is_vowel(text[0]) and
                is_vowel(text[1]) and
                not is_vowel(text[2]) and
                not is_vowel(text[3]))

    def _is_cvvv(self, text: str) -> bool:
        """
        Check if text follows a CVVV pattern (consonant-vowel-vowel-vowel).
        
        Args:
            text: Text segment to check
            
        Returns:
            bool: True if text follows CVVV pattern
            
        Example:
            >>> TextManager("")._is_cvvv("baaa")
            True
        """
        if len(text) < 4:
            return False
        return (not is_vowel(text[0]) and
                is_vowel(text[1]) and
                is_vowel(text[2]) and
                is_vowel(text[3]))

    def _is_cv(self, text: str) -> bool:
        """
        Check if text follows a CV pattern (consonant-vowel).
        
        Args:
            text: Text segment to check
            
        Returns:
            bool: True if text follows CV pattern
            
        Example:
            >>> TextManager("")._is_cv("ba")
            True
        """
        if len(text) < 2:
            return False
        return not is_vowel(text[0]) and is_vowel(text[1])

    def split_to_phonemes(self) -> str:
        """
        Split text into phonemes based on syllable patterns.
        
        The method analyzes the text and splits it into phonemes based on
        CVCC, CVVV, and CV patterns. Each phoneme is separated by a space.
        
        Returns:
            str: Text split into phonemes
            
        Example:
            >>> TextManager("barkbaaa").split_to_phonemes()
            'bark baaa'
        """
        result = []
        i = 0
        
        while i < len(self.text) - 2:
            # Check for CVCC pattern
            if i + 4 <= len(self.text) and self._is_cvcc(self.text[i:i+4]):
                result.append(self.text[i:i+4])
                i += 4
            # Check for CVVV pattern
            elif i + 4 <= len(self.text) and self._is_cvvv(self.text[i:i+4]):
                result.append(self.text[i:i+4])
                i += 4
            # Check for CV pattern
            elif i + 2 <= len(self.text) and self._is_cv(self.text[i:i+2]):
                result.append(self.text[i:i+2])
                i += 2
            else:
                # Handle unexpected pattern
                i += 1
        
        # Handle remaining text
        if i < len(self.text):
            remaining = self.text[i:]
            if len(remaining) >= 2 and self._is_cv(remaining[:2]):
                result.append(remaining[:2])
        
        return ' '.join(result)


                
