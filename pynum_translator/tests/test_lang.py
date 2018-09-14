import unittest
from ..translator import Translator
from ..dictionary import list_supported_languages
from ..custom_exceptions import Language_Not_Supported_Exception


class TestLang(unittest.TestCase):

    def test_all_aplphabets(self):
        for lang in list_supported_languages():
            try:
                t = Translator(lang)
                self.assertEqual(len(t.alphabet), 10)
            except Language_Not_Supported_Exception:
                self.fail(msg="The exception was ot expected")

    def test_exceptions(self):
        for lang in list_supported_languages():
            with self.assertRaises(Language_Not_Supported_Exception):
                _ = Translator(lang+"fail")


if __name__ == '__main__':
    unittest.main()
