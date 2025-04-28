import unittest
from src.factorial import factorial_recursivo, factorial_no_recursivo


class TestFactorial(unittest.TestCase):

    def test_factorial_iterativo_base(self):
        self.assertEqual(factorial_no_recursivo(0), 1)
        self.assertEqual(factorial_no_recursivo(1), 1)

    def test_factorial_iterativo_normal(self):
        self.assertEqual(factorial_no_recursivo(5), 120)
        self.assertEqual(factorial_no_recursivo(20), 2432902008176640000)

    def test_factorial_recursivo_base(self):
        self.assertEqual(factorial_recursivo(0), 1)
        self.assertEqual(factorial_recursivo(1), 1)

    def test_factorial_recursivo_normal(self):
        self.assertEqual(factorial_recursivo(5), 120)
        self.assertEqual(factorial_recursivo(20), 2432902008176640000)

    def test_factorial_iterativo_negativo(self):
        with self.assertRaises(ValueError):
            factorial_no_recursivo(-3)

    def test_factorial_recursivo_negativo(self):
        with self.assertRaises(ValueError):
            factorial_recursivo(-3)


if __name__ == "__main__":
    unittest.main()
