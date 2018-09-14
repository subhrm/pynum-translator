# -*- coding: utf-8 -*-
""" Define the numric aplhabet for all languages
"""

dictionary = {
    "en": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "or": ["୦", "୧", "୨", "୩", "୪", "୫", "୬", "୭", "୮", "୯"],
    "hi": ["०", "१", "२", "३", "४", "५", "६", "७", "८", "९"]
}


def list_supported_languages():
    ''' List supported languages '''
    return list(dictionary.keys())
