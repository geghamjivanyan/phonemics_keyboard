from typing import List, Optional, Union
from collections import Counter
from pathlib import Path

#
from .constants import Constants, DiacriticsSymbols as DS


def get_file_name(
    file_dir: Union[str, Path],
    model: str,
    chapter: int,
    block: int,
    iteration: int
) -> str:
    """
    Generate a prediction file name with the specified parameters.
    
    Args:
        file_dir: Directory where prediction files are stored
        model: Name of the model
        chapter: Chapter number
        block: Block number
        iteration: Iteration number
        
    Returns:
        str: Full file path for the prediction file
        
    Example:
        >>> get_file_name('predictions', 'model1', 1, 2, 3)
        'predictions/predictions_model1_001_002_03.npy'
    """
    return str(Path(file_dir) / f"predictions_{model}_{chapter:03d}_{block:03d}_{iteration:02d}.npy")


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
    return letter in Constants.vowels


def sort_by_frequency(items: List[str]) -> List[str]:
    """
    Sort a list of items by their frequency in descending order.
    
    Args:
        items: List of items to sort
        
    Returns:
        List[str]: Sorted list with unique items, ordered by frequency
        
    Example:
        >>> sort_by_frequency(['a', 'b', 'a', 'c', 'b'])
        ['a', 'b', 'c']
    """
    freq = Counter(items)
    return sorted(set(items), key=lambda x: freq[x], reverse=True)


def is_phonemic(text: str) -> bool:
    """
    Check if text contains any diacritical marks.
    
    Args:
        text: Text to check for diacritical marks
        
    Returns:
        bool: True if text contains diacritical marks, False otherwise
        
    Example:
        >>> is_phonemic('بِسْمِ')
        True
        >>> is_phonemic('بسم')
        False
    """
    return any(sym.decode('utf-8') in text for sym in DS.diacritics)


def is_keyboard_changed(mode: bool, text: str) -> bool:
    """
    Check if keyboard mode needs to be changed based on text content.
    
    Args:
        mode: Current keyboard mode
        text: Text to check
        
    Returns:
        bool: True if keyboard mode should be changed, False otherwise
        
    Example:
        >>> is_keyboard_changed(True, 'بِسْمِ')
        False
        >>> is_keyboard_changed(False, 'بسم')
        True
    """
    return mode != is_phonemic(text)


def change_hamza(text: str) -> str:
    """
    Normalize different forms of hamza to a single form.
    
    Args:
        text: Text containing hamza characters
        
    Returns:
        str: Text with normalized hamza characters
        
    Example:
        >>> change_hamza('أب')
        'ءب'
    """
    hamzas = [chr(0x0625), chr(0x0624), chr(0x0623), chr(0x0626), chr(0x0621)]
    for h in hamzas:
        text = text.replace(h, chr(0x0621))
    return text


def change_text(text: str, word: str) -> str:
    """
    Replace the last word in text with a new word and add a space.
    
    Args:
        text: Original text
        word: New word to replace the last word
        
    Returns:
        str: Modified text with the last word replaced and a space added
        
    Example:
        >>> change_text('hello world', 'there')
        'hello there '
    """
    words = text.split(' ')
    words[-1] = word
    words.append('')
    return ' '.join(words)
 
    