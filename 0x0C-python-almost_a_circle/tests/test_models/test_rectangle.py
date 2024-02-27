#!/usr/bin/python3
"""test for base class"""

import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):

    def test_inheritance_from_base(self):
        """Test inheritance from Base"""
        r = Rectangle(10, 2)
        self.assertTrue(isinstance(r, Base))

    def test_constructor_with_valid_arguments(self):
        """Test constructor with valid arguments"""
        a1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(a1.width, 1)
        self.assertEqual(a1.height, 2)
        self.assertEqual(a1.x, 3)
        self.assertEqual(a1.y, 4)
        self.assertEqual(a1.id, 5)
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
    def test_positive_width_and_height(self):
        """Test calculating area for rectangles with positive width and height"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)
    def test_positive_width_and_height(self):
        # Test displaying rectangles with positive width and height
        r1 = Rectangle(4, 6)
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "####\n####\n####\n####\n####\n####\n")

        r2 = Rectangle(2, 2)
        captured_output = StringIO()
        sys.stdout = captured_output
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "##\n##\n")
    def test_positive_width_and_height(self):
        """Test rectangle with positive width and height"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (15) 1/0 - 5/5")
    def test_large_dimensions(self):
        """Test rectangle with large dimensions"""
        r = Rectangle(100, 200)
        self.assertEqual(str(r), "[Rectangle] (12) 0/0 - 100/200")
    def test_positive_x_and_y_coordinates(self):
        """Test rectangle with positive x and y coordinates"""
        r = Rectangle(4, 6, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (17) 2/3 - 4/6")

    def test_positive_width_height_x_y(self):
        """Test rectangle with positive width, height, x, and y coordinates"""
        r1 = Rectangle(2, 3, 2, 2)
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__ 
        self.assertEqual(captured_output.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_all_arguments_correct(self):
        # Test providing all arguments correctly
        r = Rectangle(1, 1)
        r.update(10, 2, 3, 4, 5)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_some_arguments(self):
        # Test providing only some arguments
        r = Rectangle(1, 1)
        r.update(10, 2)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 2)

    def test_more_than_required_arguments(self):
        # Test providing more than the required number of arguments
        r = Rectangle(1, 1)
        r.update(10, 2, 3, 4, 5, 6)  # Extra argument
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_less_than_required_arguments(self):
        # Test providing less than the required number of arguments
        r = Rectangle(1, 1)
        r.update(10, 2, 3)  # Missing x and y arguments
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 0)  # Default value
        self.assertEqual(r.y, 0)  # Default value

    def test_invalid_arguments(self):
        # Test providing invalid arguments (non-integer values)
        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.update(10, '2', 3, 4, 5)  # '2' is a string
        with self.assertRaises(TypeError):
            r.update(10, 2, 3, {}, 5)
    def test_all_arguments_correct(self):
        # Test providing all arguments correctly
        r = Rectangle(1, 1)
        r.update(id=10, width=2, height=3, x=4, y=5)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_some_arguments(self):
        """Test providing only some arguments"""
        r = Rectangle(1, 1)
        r.update(id=10, width=2)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 2)

    def test_more_than_required_arguments(self):
        """Test providing more than the required number of arguments"""
        r = Rectangle(1, 1)
        r.update(id=10, width=2, height=3, x=4, y=5, extra=6)  # Extra argument
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_less_than_required_arguments(self):
        """Test providing less than the required number of arguments"""
        r = Rectangle(1, 1)
        r.update(id=10, width=2, height=3)  # Missing x and y arguments
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_invalid_arguments(self):
        """Test providing invalid arguments (non-integer values)"""
        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.update(id=10, width='2', height=3, x=4, y=5)  # '2' is a string
        with self.assertRaises(TypeError):
            r.update(id=10, width=2, height=3, x={}, y=5)    # {} is a dictionary

    def test_args_and_kwargs(self):
        """Test providing both *args and **kwargs"""
        r = Rectangle(1, 1)
        r.update(10, width=2, height=3, x=4, y=5)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
    def test_to_dictionary(self):
        """Test case for normal scenario"""
        r = Rectangle(5, 10, 2, 3)
        expected_dict = {'id': 19, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_to_dictionary_with_id_none(self):
        """Test case with id=None"""
        r = Rectangle(5, 10, 2, 3)
        r.id = None
        expected_dict = {'id': None, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_to_dictionary_with_default_values(self):
        """Test case with default values"""
        r = Rectangle(1, 1)
        expected_dict = {'id': 20, 'width': 1, 'height': 1, 'x': 0, 'y': 0}
        self.assertEqual(r.to_dictionary(), expected_dict)