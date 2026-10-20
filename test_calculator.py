import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 5), 2)


if __name__ == "__main__":
    unittest.main()
