import unittest
from src.fibonacci import fibonacci_recursivo, fibonacci_no_recursivo

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_iterativo_base(self):
        self.assertEqual(fibonacci_no_recursivo(1), 0)
        self.assertEqual(fibonacci_no_recursivo(2), 1)

    def test_fibonacci_iterativo_normal(self):
        self.assertEqual(fibonacci_no_recursivo(5), 3)
        self.assertEqual(fibonacci_no_recursivo(10), 34)

    def test_fibonacci_recursivo_base(self):
        self.assertEqual(fibonacci_recursivo(1), 0)
        self.assertEqual(fibonacci_recursivo(2), 1)

    def test_fibonacci_recursivo_normal(self):
        self.assertEqual(fibonacci_recursivo(5), 3)
        self.assertEqual(fibonacci_recursivo(10), 34)

    def test_fibonacci_iterativo_negativo(self):
        with self.assertRaises(ValueError):
            fibonacci_no_recursivo(0)
        with self.assertRaises(ValueError):
            fibonacci_no_recursivo(-5)

    def test_fibonacci_recursivo_negativo(self):
        with self.assertRaises(ValueError):
            fibonacci_recursivo(0)
        with self.assertRaises(ValueError):
            fibonacci_recursivo(-5)


if __name__ == "__main__":
    unittest.main()
