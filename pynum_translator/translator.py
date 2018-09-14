from .custom_exceptions import Language_Not_Supported_Exception
from .dictionary import dictionary


class Translator:
    def __init__(self, lang: str):
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

    def from_int(self, number: int) -> str:
        '''
        Translate a given integer.

        Arguments:
            number {int} -- Input Integer

        Returns:
            str -- Unicode string containg the numerical representation of the given number
        '''

        number_string = str(number)
        result_string = ""
        for c in number_string:
            result_string += self.alphabet[int(c)]

        return result_string
