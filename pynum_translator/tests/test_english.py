import unittest
from ..translator import Translator
import random


class TestEnglish(unittest.TestCase):

    def test_positives(self):
        t = Translator(lang="en")

        for _ in range(100):
            num = random.randint(0, 10000000)
            self.assertEqual(t.from_int(num), str(num))


if __name__ == '__main__':
    unittest.main()
