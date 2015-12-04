__author__ = 'root'

import unittest

from motor.PossibilitiesGenerator import PossibilitiesGenerator


class TestPossibilitiesGenerator(unittest.TestCase):

    LETTERS = 28
    NUMBERS = 10

    def setUp(self):
        setup = 1

    def test_lower_letters(self):
        possibilities = self.LETTERS * 3
        self.assertEqual(possibilities, PossibilitiesGenerator.generate(3, True))

    def test_upper_letters(self):
        possibilities = self.LETTERS * 3
        self.assertEqual(possibilities, PossibilitiesGenerator.generate(3, False, True))

    def test_lower_upper_letters(self):
        possibilities = (self.LETTERS + self.LETTERS) * 3
        self.assertEqual(possibilities, PossibilitiesGenerator.generate(3, True, True))

    def test_numbers(self):
        possibilities = self.NUMBERS * 3
        self.assertEqual(possibilities, PossibilitiesGenerator.generate(3, False, False, True))

    def test_lower_upper_letters_numbers(self):
        possibilities = (self.LETTERS + self.LETTERS + self.NUMBERS) * 3
        self.assertEqual(possibilities, PossibilitiesGenerator.generate(3, True, True, True))


