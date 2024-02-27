#!/usr/bin/python3

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_valid_arguments(self):
        """Test creating a square with valid arguments"""
        s = Square(5)
        self.assertEqual(s.id, 12)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_invalid_arguments(self):
        """Test creating a square with invalid arguments"""
        with self.assertRaises(TypeError):
            s = Square('5')
        with self.assertRaises(ValueError):
            s = Square(-5)

    def test_str_method(self):
        """Test the __str__ method"""
        s = Square(5, 1, 2, 10)
        self.assertEqual(str(s), "[Square](10) 1/2 - 5")
    def test_set_valid_size(self):
        """Test setting a valid size"""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_set_invalid_size(self):
        """Test setting an invalid size"""
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = '10'
        with self.assertRaises(ValueError):
            s.size = -10

    def test_get_size(self):
        """Test getting the size after setting it"""
        s = Square(5)
        self.assertEqual(s.size, 5)
    def test_update_with_args(self):
        """Test updating attributes using positional arguments"""
        s = Square(5)
        s.update(1, 10, 2, 3)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_update_with_kwargs(self):
        """Test updating attributes using keyword arguments"""
        s = Square(5)
        s.update(id=1, size=10, x=2, y=3)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_update_with_mixed_args_kwargs(self):
        """Test updating attributes using mixed positional and keyword arguments"""
        s = Square(5)
        s.update(1, size=10, x=2, y=3)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_update_with_invalid_args(self):
        """Test updating attributes with invalid arguments"""
        s = Square(5)
        with self.assertRaises(TypeError):
            s.update(1, '10', 2, 3)
        with self.assertRaises(ValueError):
            s.update(1, -10, 2, 3)
    def test_to_dictionary(self):
        """Test case for normal scenario"""
        s = Square(5, 2, 3, 1)
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_to_dictionary_with_id_none(self):
        """Test case with id=None"""
        s = Square(5, 2, 3)
        s.id = None
        expected_dict = {'id': None, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_to_dictionary_with_default_values(self):
        """Test case with default values"""
        s = Square(1)
        expected_dict = {'id': 6, 'size': 1, 'x': 0, 'y': 0}
        self.assertEqual(s.to_dictionary(), expected_dict)
