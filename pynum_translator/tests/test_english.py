# -*- coding: utf-8 -*-
import unittest
from .. import Translator
import random


class TestEnglish(unittest.TestCase):

    def test_en_ints(self):
        '''English - Test Integers
        '''

        t = Translator(lang="en")

        for _ in range(100):
            num = random.randint(0, 10000000)
            self.assertEqual(t.translate(num), str(num))

    def test_en_strs(self):
        ''' English - Test with string inputs
        '''

        t = Translator(lang="en")

        for _ in range(100):
            num = random.randint(0, 10000000)
            self.assertEqual(t.translate(str(num)), str(num))

    def test_en_formmated(self):
        '''English - Test with formatted strings
        '''

        t = Translator(lang="en")

        for _ in range(100):
            num = random.randint(1, 10000000)
            fmt_str = "{:,}".format(num)
            self.assertEqual(t.translate(fmt_str), fmt_str)

    def test_en_floats(self):
        ''' English - Test with formatted decimals
        '''

        t = Translator(lang="en")

        for _ in range(100):
            num = random.randint(1, 10000000)
            fmt_str = "{:.3f}".format(num/100)
            self.assertEqual(t.translate(fmt_str), fmt_str)


if __name__ == '__main__':
    unittest.main()
