import unittest
from main import OddEvenLangPacks

class TestOddEvenLangPacks(unittest.TestCase):

    def setUp(self):
        self.oddEven = OddEvenLangPacks("EN")

    def test_changeLanguage_valid(self):
        self.oddEven.changeLanguage("ID")
        self.assertEqual(self.oddEven.language, "ID")

    def test_changeLanguage_invalid(self):
        self.oddEven.changeLanguage("XX")
        self.assertEqual(self.oddEven.language, "EN")

    def test_check_EN(self):
        self.assertEqual(self.oddEven.check(1), "odd")
        self.assertEqual(self.oddEven.check(2), "even")

    def test_check_ID(self):
        self.oddEven.changeLanguage("ID")
        self.assertEqual(self.oddEven.check(1), "ganjil")
        self.assertEqual(self.oddEven.check(2), "genap")

    def test_checks(self):
        self.assertEqual(self.oddEven.checks([1, 2, 3]), ["odd", "even", "odd"])

    def test_isOdd(self):
        self.assertTrue(self.oddEven.isOdd(1))
        self.assertFalse(self.oddEven.isOdd(2))

    def test_isEven(self):
        self.assertTrue(self.oddEven.isEven(2))
        self.assertFalse(self.oddEven.isEven(1))

if __name__ == '__main__':
    unittest.main()