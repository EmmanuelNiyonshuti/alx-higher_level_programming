#!/usr/bin/python3
"""test for base class"""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_all_attributes(self):
        a1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(a1.width, 1)
        self.assertEqual(a1.height, 2)
        self.assertEqual(a1.x, 3)
        self.assertEqual(a1.y, 4)
        self.assertEqual(a1.id, 5)
    def test_two_attributes(self):
        a2 = Rectangle(1, 3)
        self.assertEqual(a2.width, 1)
        self.assertEqual(a2.height, 3)
        self.assertEqual(a2.x, 0)
        self.assertEqual(a2.y, 0)

    def test_width_passed_as_0(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
    def test_width_passed_as_negative_num(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
    def test_width_passed_as_dict(self):
        with self.assertRaises(TypeError):
            Rectangle({}, 2)
    def test_width_passed_as_list(self):
        with self.assertRaises(TypeError):
            Rectangle([], 2)
    def test_width_passed_as_tuple(self):
        with self.assertRaises(TypeError):
            Rectangle((), 2)
    def test_width_passed_as_str(self):
        with self.assertRaises(TypeError):
            Rectangle("python", 2)
    def test_width_passed_as_float(self):
        with self.assertRaises(TypeError):
            Rectangle(1.34, 2)
    def test_height_passed_as_negative_num(self):
        with self.assertRaises(ValueError):
            Rectangle(2, -2)
    def test_height_passed_as_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
    def test_height_passed_as_float(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 3.14)
    
    def test_height_passed_as_list(self):
        with self.assertRaises(TypeError):
            Rectangle(2, [])
    def test_height_passed_as_tuple(self):
        with self.assertRaises(TypeError):
            Rectangle(2, (1, 2))
    def test_height_passed_as_str(self):
        with self.assertRaises(TypeError):
            Rectangle(5, "")
    def test_x_passed_as_negative_num(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -1)
    def test_x_passed_as_flaot(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 2.5)
    def test_x_passed_as_str(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 2, "")
    def test_x_passed_as_list(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 2, [1, 3])
    def test_y_passed_as_negative_num(self):
        with self.assertRaises(ValueError):
            Rectangle(4, 2, 5, -3)
    def test_y_passed_as_float(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 3, 4, 3.56)
    def test_y_passed_as_list(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 4, [])
    def test_y_passed_as_str(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 3, 4, "school")
    def test_y_passed_as_dict(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 3, 4, {})
    def test_area_with_valid_inputs(self):
        a = Rectangle(2, 4)
        self.assertEqual(a.area(), 8)
    