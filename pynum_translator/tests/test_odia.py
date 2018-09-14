# -*- coding: utf-8 -*-
import unittest
from .. import Translator


class TestOriya(unittest.TestCase):

    def test_or_ints(self):
        ''' Oriya - Test with integers
        '''

        t = Translator(lang="or")
        cases = [(101, "୧୦୧"), (11, "୧୧"), (0, "୦")]
        for e, o in cases:
            self.assertEqual(t.translate(e), o)

    def test_or_examples(self):
        ''' Oriya - Test the "or" examples provided in the readme file
        '''
        or_translator = Translator(lang="or")
        self.assertEqual(or_translator.translate(123), "୧୨୩")
        self.assertEqual(or_translator.translate("456"), "୪୫୬")
        self.assertEqual(or_translator.translate(
            "There are 456 ducks in the zoo!"), "There are ୪୫୬ ducks in the zoo!")


if __name__ == '__main__':
    unittest.main()
