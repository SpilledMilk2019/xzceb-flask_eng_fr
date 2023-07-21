import unittest

from translator import english_to_french,french_to_english

class TestTranslator(unittest.TestCase):

    def test_englishToFrench(self):
        result1 = english_to_french("Hello")
        self.assertEqual(result1,"Bonjour")

        result2 = english_to_french("Goodbye")
        self.assertEqual(result2,"Au revoir")

    def test_frenchToEnglish(self):
        result1 = french_to_english("Bonjour")
        self.assertEqual(result1,"Hello")

        result2 = french_to_english("Au revoir")
        self.assertEqual(result2,"Goodbye")

if __name__ == '__main__':
    unittest.main()

