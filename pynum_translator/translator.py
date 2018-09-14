# -*- coding: utf-8 -*-
from .custom_exceptions import Language_Not_Supported_Exception
from .dictionary import dictionary


class Translator:
    def __init__(self, lang):
        '''
        Check the language code and load the coresponding alphabet
        Arguments:
            lang {str} -- Language code 

        Raises:
            Language_Not_Supported_Exception -- Raised if teh language is not supported
        '''

        lang = lang.lower()
        if lang not in dictionary:
            raise Language_Not_Supported_Exception(lang)

        self.alphabet = dictionary[lang]

    def translate(self, input):
        '''
        Translate a given integer.

        Arguments:
            number {int} -- Input Integer

        Returns:
            str -- Unicode string containg the numerical representation of the given number
        '''

        number_string = str(input)
        result_string = ""
        for c in number_string:
            s = c
            try:
                s = self.alphabet[int(c)]
            except ValueError:
                s = c

            result_string += s

        return result_string
