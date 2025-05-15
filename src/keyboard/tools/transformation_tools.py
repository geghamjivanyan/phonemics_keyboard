from typing import Dict, List, Optional, Set
from .utils import is_vowel
from .constants import Translit as T


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
    result = ''
    i = 0
    
    while i < len(text):
        # Try to match two characters first
        if text[i:i+2] in T.from_translit:
            result += T.from_translit[text[i:i+2]]
            i += 2
        else:
            # Try to match single character
            try:
                result += T.from_translit[text[i]]
            except KeyError:
                pass
            i += 1
    
    return result


def from_arabic_to_translit(text: str) -> str:
    """
    Convert Arabic text to transliterated form.
    
    Args:
        text: Text in Arabic
        
    Returns:
        str: Text converted to transliterated form
        
    Example:
        >>> from_arabic_to_translit('بسم')
        'bism'
    """
    # Remove special characters
    text = text.replace('N', '').replace('Y', '').replace('W', '')
    
    result = ''
    i = 0
    
    # Handle initial alif
    if text and text[0] == chr(0x0627):
        result += chr(0x2bc) + chr(0x064E)
        i += 1
    
    while i < len(text):
        # Handle shadda
        if i < len(text) - 1 and text[i+1] == chr(0x0651):
            result += 2 * T.to_translit[text[i]]
            i += 2
            continue
            
        # Handle space before alif
        if i > 0 and text[i-1] == ' ' and text[i] == chr(0x0627):
            result += ' '
            i += 1
            continue
            
        # Try to match two characters
        if text[i:i+2] in T.to_translit:
            if (i > 1 and 
                T.to_translit.get(text[i-1]) in T.a_rules and 
                text[i] == chr(0x064E)):
                result += 'A'
                i += 1
            else:
                result += T.to_translit[text[i:i+2]]
                i += 2
        else:
            # Handle single character
            try:
                if (i > 0 and 
                    text[i-1] == chr(0x064E) and 
                    text[i] == chr(0x0627)):
                    result += 'a'
                elif (i > 0 and 
                      T.to_translit.get(text[i-1]) in T.a_rules and 
                      text[i] == chr(0x064E)):
                    result += 'A'
                elif (i > 0 and 
                      T.to_translit.get(text[i-1]) in T.l_rules and 
                      text[i] == chr(0x0644)):
                    result += 'L'
                else:
                    result += T.to_translit[text[i]]
            except (KeyError, IndexError):
                pass
            i += 1
            
        # Fix common patterns
        if result[-2:] == 'aA':
            result = result[:-2] + 'aa'
        elif result[-2:] == 'Aa':
            result = result[:-2] + 'AA'
    
    return result


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
