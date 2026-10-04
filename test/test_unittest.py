import unittest

from src.calculator import fun1, fun2, fun3, fun4, fun5, fun6, fun7, fun8


class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(fun1(2, 3), 5)

    def test_fun2(self):
        self.assertEqual(fun2(5, 3), 2)

    def test_fun3(self):
        self.assertEqual(fun3(4, 3), 12)

    def test_fun4(self):
        self.assertEqual(fun4(1, 2, 3), 6)

    def test_fun5(self):
        self.assertEqual(fun5(10, 2), 5)

    def test_fun6(self):
        self.assertEqual(fun6(2, 3), 8)

    def test_fun7(self):
        self.assertEqual(fun7(10, 3), 1)

    def test_fun8(self):
        self.assertEqual(fun8(10, 20), 15)


if __name__ == "__main__":
    unittest.main()