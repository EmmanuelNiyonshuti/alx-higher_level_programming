#!/usr/bin/python3
"""
This module comprises a tests for Square subclass.
"""

import unittest
from models.square import Square
from io import StringIO
import sys

class TestSquare(unittest.TestCase):
    """Test Square subclass"""
    def test_size(self):
        s1 = Square(5)
        capt_output = StringIO()
        sys.stdout = capt_output
        print(s1)
        sys.stdout = sys.__stdout__
        capt_output.seek(0)
        self.assertEqual(capt_output.read(), '[Square](1) 0/0 - 5\n')

        s1.size = 10
        c_output = StringIO()
        sys.stdout = c_output
        print(s1)
        sys.stdout = sys.__stdout__
        c_output.seek(0)
        self.assertEqual(c_output.read(), '[Square](1) 0/0 - 10\n')

        get_output = StringIO()
        sys.stdout = get_output
        print(s1.size)
        sys.stdout = sys.__stdout__
        get_output.seek(0)
        self.assertEqual(get_output.read(), '10\n')

        with self.assertRaises(TypeError):
            s1.width = "9"
        with self.assertRaises(ValueError):
            s1.width = 0
