# tests/test_flatten.py

import unittest
from src.flatten import flatten

class TestFlatten(unittest.TestCase):

    def test_flatten_basic(self):
        self.assertEqual(flatten([[1, 2], [3, 4]]), [1, 2, 3, 4])

    def test_flatten_empty(self):
        self.assertEqual(flatten([]), [])

    def test_flatten_single_level(self):
        self.assertEqual(flatten([1, 2, 3]), [1, 2, 3])

    def test_flatten_multiple_levels(self):
        self.assertEqual(flatten([[[1, 2], 3], [4]]), [1, 2, 3, 4])

    def test_flatten_no_nested(self):
        self.assertEqual(flatten([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_flatten_complex(self):
        self.assertEqual(flatten([1, [2, [3, [4]]]]), [1, 2, 3, 4])

if __name__ == "__main__":
    unittest.main()
