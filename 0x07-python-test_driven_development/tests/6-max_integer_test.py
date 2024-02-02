#!/usr/bin/python3
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
        """Test for an empty list"""
        self.assertEqual(max_integer([]), None)
    def test_list_negative(self):
        """Test for a list with negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-100, -10000, 0]), 0)
    def test_duplicate(self):
        """Test for a duplicate list"""
        self.assertEqual(max_integer([1, 2, 10, 8, 10]), 10)
    def mixed_types(self):
        """Test for a list with mixed types"""
        self.assertEqual(max_integer([1, "a", "k", 9]), 9)
        self.assertEqual(max_integer([1.0, 2.5, 7.2, -1.5, 10.2]), 10.2)

    if __name__=='__main__':
        unittest.main()
