import unittest
from odd_even_lang_packs.main import OddEvenLangPacks

class TestOddEvenLangPacks(unittest.TestCase):

    def setUp(self):
        self.oddEven = OddEvenLangPacks("EN")

    def __lang_test_check(self, langCode : str, odd : str, even : str):
        self.oddEven.changeLanguage(langCode.upper())
        self.assertEqual(self.oddEven.check(1), odd.lower())
        self.assertEqual(self.oddEven.check(2), even.lower())

    def test_changeLanguage_valid(self):
        self.oddEven.changeLanguage("ID")
        self.assertEqual(self.oddEven.getLanguage(), "ID")

    def test_changeLanguage_invalid(self):
        self.oddEven.changeLanguage("XX")
        self.assertEqual(self.oddEven.getLanguage(), "EN")

    def test_check_EN(self):
        # English for odd and even
        self.__lang_test_check("EN", odd="odd", even="even")

    def test_check_ID(self):
        # Indonesian for odd and even
        self.__lang_test_check("ID", odd="ganjil", even="genap")
    
    def test_check_DK(self):
        # Danish (Denmark) for odd and even
        self.__lang_test_check("DK", odd="ulige", even="lige")

    def test_checks(self):
        self.assertEqual(self.oddEven.checks([1, 2, 3]), ["odd", "even", "odd"])

    def test_isOdd(self):
        self.assertTrue(self.oddEven.isOdd(1))
        self.assertFalse(self.oddEven.isOdd(2))

    def test_isEven(self):
        self.assertTrue(self.oddEven.isEven(2))
        self.assertFalse(self.oddEven.isEven(1))

    def test_getLanguage(self):
        self.assertEqual(self.oddEven.getLanguage(), "EN")

    def test_getLanguageCodes(self):
        self.assertEqual(type(self.oddEven.getLanguageCodes()), list)

    def test_getLanguageCodesAndFullNames(self):
        self.assertEqual(type(self.oddEven.getLanguageCodesAndFullNames()), dict)

if __name__ == '__main__':
    unittest.main()