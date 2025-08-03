import unittest
from calculator import scitani

class TestScitaniFunction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(scitani(6, 4), 10)

    def test_negative_numbers(self):
        self.assertEqual(scitani(-1, -1), -2)

    def test_mixed_sign_numbers(self):
        self.assertEqual(scitani(-6, 8), 2)

    def test_zero(self):
        self.assertEqual(scitani(0, 0), 0)
        self.assertEqual(scitani(5, 0), 5)

if __name__ == '__main__':
    unittest.main()
