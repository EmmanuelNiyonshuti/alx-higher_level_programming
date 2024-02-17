#!/usr/bin/python3
"""module comprises a class to test max_integer([..]).
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestList(unittest.TestCase):
    """tests max_integer([..])"""

    def test_value(self):
        """Tests the maximum value in a list of integers"""
        self.assertEqual(max_integer([1, 2,3, 4]), 4)
        self.assertEqual(max_integer([1, 4,3, 2]), 4)
        self.assertEqual(max_integer([-1, 0,-3, -4]), 0)
        self.assertEqual(max_integer([-1, -2,-3, -4]), -1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([[5, 0], [4, 20]]), [5, 0])
        with self.assertRaises(TypeError):
            max_integer(["hello", 1, 2])



