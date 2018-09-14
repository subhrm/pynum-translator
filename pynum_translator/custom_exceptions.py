'''
Define custom exceptions.
'''


class Language_Not_Supported_Exception(Exception):
    ''' This language is not supported.
    '''

    def __init__(self, lang=""):
        super().__init__(f"The language {lang} is not implemented")
