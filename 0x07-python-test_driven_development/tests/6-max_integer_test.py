"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInt(unittest.TestCase):

    def test_regularlist(self):
        """Test with a regular list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
    def test_list_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-100, -10000, 0]), 0)
    def test_duplicate(self):
        self.assertEqual(max_integer([1, 2, 10, 8, 10]), 10)
    def mixed_types(self):
        self.assertEqual(max_integer([1, "a", "k", 9]), 9)
