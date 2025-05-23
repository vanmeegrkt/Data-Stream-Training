# test_calculator.py
import unittest
from calculator import divide

class TestCalculator(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(7, 3), 2.3333, places=4)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()