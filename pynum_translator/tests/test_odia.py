import unittest
from ..translator import Translator


class TestOriya(unittest.TestCase):

    def test_positives(self):
        t = Translator(lang="or")
        cases = [(101, "୧୦୧"), (11, "୧୧")]
        for e, o in cases:
            self.assertEqual(t.from_int(e), o)


if __name__ == '__main__':
    unittest.main()
