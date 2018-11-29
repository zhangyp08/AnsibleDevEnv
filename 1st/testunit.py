import unittest

from MathTest import Calculator

class TestMathFunc(unittest.TestCase):

    def test_add(self):
        c = Calculator()
        self.assertEqual(3, c.add(1,2))
        self.assertNotEqual(4, c.add(2,3))

    def test_minus(self):
        c = Calculator()
        self.assertEqual(0, c.substract(2, 2))
        self.assertNotEqual(1, c.substract(5, 4))

    def test_multi(self):
        c = Calculator()
        self.assertEqual(2, c.multiply(1, 2))
        self.assertNotEqual(4, c.multiply(2, 3))

    def test_divide(self):
        c = Calculator()
        self.assertEqual(0.5, c.divide(1, 2))
        self.assertNotEqual(4, c.divide(2, 3))


if __name__ == '__main__':
    unittest.main()