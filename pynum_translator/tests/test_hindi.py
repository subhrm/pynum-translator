# -*- coding: utf-8 -*-
import unittest
from .. import Translator


class TestHindi(unittest.TestCase):

    def test_hi_ints(self):
        ''' Hindi - Test with integers
        '''

        t = Translator(lang="or")
        cases = [(101, "१०१"), (11, "११"), (0, "०")]
        for e, o in cases:
            self.assertEqual(t.translate(e), o)

    def test_hi_examples(self):
        ''' Hindi - Test the "hi" examples provided in the readme file
        '''
        hi_translator = Translator(lang="hi")
        self.assertEqual(hi_translator.translate(123), "१२३")
        self.assertEqual(hi_translator.translate(76.05), "६७.०५")


if __name__ == '__main__':
    unittest.main()
