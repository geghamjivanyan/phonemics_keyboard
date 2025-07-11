import logging
from typing import Dict, List, Optional, Set
from .utils import is_vowel
from .constants import Translit as T

from .constants import TR

logger = logging.getLogger(__name__)


def from_translit_to_arabic(text: str) -> str:
    """
    Convert transliterated text to Arabic.
    
    Args:
        text: Text in transliterated form
        
    Returns:
        str: Text converted to Arabic
        
    Example:
        >>> from_translit_to_arabic('bism')
        'بسم'
    """
    try:
        result = ''
        i = 0
        
        while i < len(text):
            # Try to match two characters first
            if i+1 < len(text) and text[i:i+2] in T.from_translit:
                result += T.from_translit[text[i:i+2]]
                i += 2
            else:
                # Try to match single character
                try:
                    result += T.from_translit[text[i]]
                except KeyError as e:
                    logger.warning(f"Character not found in from_translit mapping: {text[i]}")
                i += 1

        return result
    except Exception as e:
        logger.error(f"Error in from_translit_to_arabic: {str(e)}", exc_info=True)
        return text

def before_translit(text):

    for k,v in TR.bt_1.items():
        text = text.replace(k, v)

    for k,v in TR.bt_2.items():
        text = text.replace(k, v)

    for k,v in TR.bt_3.items():
        text = text.replace(k, v)

    return text

def translit(text):

    for k,v in TR.tr_1.items():
        text = text.replace(k, v)


    for k,v in TR.tr_2.items():
        text = text.replace(k, v)

    for k,v in TR.tr_3.items():
        text = text.replace(k, v)

    return text

def after_translit(text):

    for k,v in TR.at_1.items():
        text = text.replace(k,v)

    return text

def shadda(text):

    letters = list(text)

    if len(letters) >= 3:
        for i in range(len(letters)-2):
            if not is_vowel(letters[i]) and letters[i+1] == chr(0x0651):
                letters[i+1] = letters[i]
    
    text = ''.join(letters)

    return text




def from_arabic_to_translit(text: str) -> str:
    text = before_translit(text)
    text = translit(text)
    text = after_translit(text)
    text = text.replace(' ', '')
    return text


def classify(text: str) -> str:
    """
    Classify text into a pattern based on word lengths.
    
    Args:
        text: Text to classify
        
    Returns:
        str: Pattern string where:
            1 = word length <= 2
            2 = word length = 3
            3 = word length > 3
            
    Example:
        >>> classify('a b ccc dddd')
        '123'
    """
    pattern = ''
    for word in text.split():
        if not word:
            continue
        if len(word) <= 2:
            pattern += '1'
        elif len(word) == 3:
            pattern += '2'
        else:
            pattern += '3'
    return pattern


def split(text: str) -> str:
    """
    Split text into syllables based on vowel patterns.
    
    Args:
        text: Text to split
        
    Returns:
        str: Text split into syllables with spaces
        
    Example:
        >>> split('bism')
        'bis m'
    """
    # Handle special case for 'L'
    text = text.replace('L', 'l')
    
    # Handle short text
    if len(text) == 3:
        # VVC pattern
        if (is_vowel(text[0]) and 
            is_vowel(text[1]) and 
            not is_vowel(text[2])):
            return f"{text[:2]} {text[2]}"
        # C1C2V pattern
        elif (not is_vowel(text[0]) and 
              not is_vowel(text[1]) and 
              is_vowel(text[2]) and 
              text[0] != text[1]):
            return f"{text[0]} {text[1:]}"
        # C1C2C3 pattern
        elif (not is_vowel(text[0]) and 
              not is_vowel(text[1]) and 
              not is_vowel(text[2]) and 
              text[0] == text[1]):
            return text
        # VCV pattern
        elif (is_vowel(text[0]) and 
              not is_vowel(text[1]) and 
              is_vowel(text[2])):
            return f"{text[0]} {text[1:]}"
    
    # Add padding for easier processing
    text = text + '++'
    result = ''
    i = 0
    
    while i < len(text) - 2:
        # VVC pattern
        if (is_vowel(text[i]) and 
            is_vowel(text[i+1]) and 
            not is_vowel(text[i+2])):
            result += text[i:i+2] + ' '
            i += 2
        # C1C2V pattern with different consonants
        elif (not is_vowel(text[i]) and 
              not is_vowel(text[i+1]) and 
              is_vowel(text[i+2]) and 
              text[i] != text[i+1]):
            result += text[i] + ' '
            i += 1
        # C1C2V pattern with same consonants
        elif (not is_vowel(text[i]) and 
              not is_vowel(text[i+1]) and 
              is_vowel(text[i+2]) and 
              text[i] == text[i+1]):
            result += ' ' + text[i:i+2]
            i += 2
        # V1C2V2 pattern
        elif (is_vowel(text[i]) and 
              not is_vowel(text[i+1]) and 
              is_vowel(text[i+2])):
            result += text[i] + ' '
            i += 1
        else:
            result += text[i]
            i += 1
    
    return result.strip()


def apply_transformation_rules(text: str) -> str:
    """
    Apply various transformation rules to Arabic text.
    
    Args:
        text: Arabic text to transform
        
    Returns:
        str: Transformed text
        
    Example:
        >>> apply_transformation_rules('الله')
        'الْلاه'
    """
    # Define character sets
    X_CHARS = ["ث", "ص", "ض", "ن", "ت", "س", "ش", "ر", "ز", "د", "ذ", "ط", "ظ"]
    C_CHARS = ["ج", "ح", "خ", "ه", "ع", "غ", "ف", "ق", "ك", "م", "ل", "و", "ي", "ء"]
    
    # Rule 1: Handle initial alif
    if text.startswith("ا"):
        text = "ءَ" + text[1:]
    
    # Rule 2: Handle alif-lam combinations
    for x in X_CHARS:
        term = "ال" + x
        if text.startswith(term):
            text = "ءَ" + x + x + text[len(term):]
    
    # Rule 3: Apply word mappings
    WORD_MAPPINGS = {
        "هَذا": "هَاذا",
        "الرَّحْمَنِ": "ارْرَحْمَانِ",
        "أُولَئِكَ": "أُلَائِكَ",
        "هَؤُلَاء": "هَاؤُلَاء",
        "سَمَوَات": "سَمَاوَات",
        "الله": "اللاه",
        "اللَه": "الْلاه",
        "اللَّه": "الْلاه",
        "لِلَّهِ": "لِلْلَاهِ",
        "الَّذِي": "الْلَذِي",
        "الَّذِينَ": "الْلَذِينَ",
        "لِلَّذِي": "لِلْلَذِي"
    }
    
    for word, replacement in WORD_MAPPINGS.items():
        if text.startswith(word):
            text = replacement + text[len(word):]
    
    # Rule 4: Handle final waw-alif
    if text.endswith("ُوا"):
        text = text[:-2] + "ُو"
    
    # Rule 5: Handle final vowels with nun
    vowels = [chr(0x064E), chr(0x0650), chr(0x064F)]
    for v in vowels:
        if text.endswith(v + " "):
            text = text[:-1] + chr(0x0646) + " "
    
    # Rule 9: Handle various vowel-alif combinations
    VOWEL_ALIF_RULES = {
        "َ ا": "َ",
        "َا ا": "َ",
        "ُ ا": "ُ",
        "ُوا ا": "ُ",
        "ِ ا": "ِ",
        "ِي ا": "ِ",
        "َى ا": "َ"
    }
    
    for pattern, replacement in VOWEL_ALIF_RULES.items():
        text = text.replace(pattern, replacement)
    
    # Rule 11: Handle prefixes with alif-lam
    PREFIXES = ["فَ", "وَكَ", "كَ", "فَكَ", "كَبِ", "وَ", "فَوَ", "وَبِ", "بِ", "أَبِ", "فَبِ"]
    
    for prefix in PREFIXES:
        text = text.replace(prefix + "ال", prefix + " " + "ال")
    
    return text