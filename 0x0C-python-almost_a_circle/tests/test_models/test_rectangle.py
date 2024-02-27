#!/usr/bin/python3
"""
This module comprises a Test for the child class Rectangle.
"""

import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test Rectangle Class"""
    def setUp(self):
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 0, 0, 12)
        self.r4 = Rectangle(4, 5)

    def test_private_attributes(self):
        self.assertEqual(self.r3.width, 10)
        self.r3.width = 13
        self.assertEqual(self.r3.width, 13)
        self.assertEqual(self.r3.height, 2)
        self.r3.height = 5
        self.assertEqual(self.r3.height, 5)
        self.assertEqual(self.r3.x, 0)
        self.r3.x = 4
        self.assertEqual(self.r3.x, 4)
        self.assertEqual(self.r3.y, 0)
        self.r3.y = 6
        self.assertEqual(self.r3.y, 6)

    def test_attribute_validation(self):
        invalid_params = [
            (0, 2),
            (-1, 2),
            (2.7, 2),
            ("2", 2),
            ([], 2),
            ((), 2),
            (None, 2),
            (10, "2"),
            (10, 2.8),
            (10, {}),
            (10, 2, "4"),
            (10, 2, ""),
            (10, 2, 4, "8"),
            (10, 2, 4, 2.34),
            (1, 0),
            (1, -2),
            (1, 2, -1),
            (1, 2, 1, -1)
        ]
        for params in invalid_params:
            with self.assertRaises((TypeError, ValueError)):
                Rectangle(*params)

    def test_area(self):
        Rect1 = Rectangle(3, 2)
        self.assertEqual(Rect1.area(), 6)
        Rect2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(Rect2.area(), 56)

    def test_display(self):
        r1 = Rectangle(2, 2)
        # Instantiate StringIO object
        capt_output = StringIO()
        # Redirect stdout to StringIO object
        sys.stdout = capt_output
        r1.display()
        # Reset stdout
        sys.stdout = sys.__stdout__
        # Retrieve the captured output for the first Rectangle object
        capt_output.seek(0)
        # Assert against the captured output for the first Rectangle object
        self.assertEqual(capt_output.read().strip(), '##\n##')

        r2 = Rectangle(4, 6)
        capt_output = StringIO()
        sys.stdout = capt_output
        r2.display()
        sys.stdout = sys.__stdout__
        capt_output.seek(0)
        self.assertEqual(capt_output.read().strip(), '####\n####\n####\n####\n####\n####')
        r3 = Rectangle(2, 3, 2, 2)
        catch_output = StringIO()
        sys.stdout = catch_output
        r3.display()
        sys.stdout = sys.__stdout__
        catch_output.seek(0)
        self.assertEqual(catch_output.read(), '\n\n  ##\n  ##\n  ##\n')

    def test_str(self):
        rectangle1 = Rectangle(4, 6, 2, 1, 12)
        output = StringIO()
        sys.stdout = output
        print(rectangle1)
        sys.stdout = sys.__stdout__
        output.seek(0)
        self.assertEqual(output.read(), '[Rectangle] (12) 2/1 - 4/6\n')

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        get_output = StringIO()
        sys.stdout = get_output
        print(r1)
        sys.stdout = sys.__stdout__
        get_output.seek(0)
        self.assertEqual(get_output.read(), '[Rectangle] (89) 10/10 - 10/10\n')
        r1.update(89, 2)
        get_output = StringIO()
        sys.stdout = get_output
        print(r1)
        sys.stdout = sys.__stdout__
        get_output.seek(0)
        self.assertEqual(get_output.read(), '[Rectangle] (89) 10/10 - 2/10\n')

        r1.update(89, 2, 3)
        get_output = StringIO()
        sys.stdout = get_output
        print(r1)
        sys.stdout = sys.__stdout__
        get_output.seek(0)
        self.assertEqual(get_output.read(), '[Rectangle] (89) 10/10 - 2/3\n')

        r1.update(89, 2, 3, 4)
        get_output = StringIO()
        sys.stdout = get_output
        print(r1)
        sys.stdout = sys.__stdout__
        get_output.seek(0)
        self.assertEqual(get_output.read(), '[Rectangle] (89) 4/10 - 2/3\n')

        r1.update(89, 2, 3, 4, 5)
        get_output = StringIO()
        sys.stdout = get_output
        print(r1)
        sys.stdout = sys.__stdout__
        get_output.seek(0)
        self.assertEqual(get_output.read(), '[Rectangle] (89) 4/5 - 2/3\n')
    
    def test_updated_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        get_output = StringIO()
        sys.stdout = get_output
        print(r1)
        sys.stdout = sys.__stdout__
        get_output.seek(0)
        self.assertEqual(get_output.read(), '[Rectangle] (49) 10/10 - 10/1\n')

        r1.update(width=1, x=2)
        get_output = StringIO()
        sys.stdout = get_output
        print(r1)
        sys.stdout = sys.__stdout__
        get_output.seek(0)
        self.assertEqual(get_output.read(), '[Rectangle] (49) 2/10 - 1/1\n')

        r1.update(y=1, width=2, x=3, id=89)
        get_output = StringIO()
        sys.stdout = get_output
        print(r1)
        sys.stdout = sys.__stdout__
        get_output.seek(0)
        self.assertEqual(get_output.read(), '[Rectangle] (89) 3/1 - 2/1\n')

        r1.update(x=1, height=2, y=3, width=4)
        get_output = StringIO()
        sys.stdout = get_output
        print(r1)
        sys.stdout = sys.__stdout__
        get_output.seek(0)
        self.assertEqual(get_output.read(), '[Rectangle] (89) 1/3 - 4/2\n')

    def test_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        s = StringIO()
        sys.stdout = s
        print(r1_dictionary)
        sys.stdout = sys.__stdout__
        s.seek(0)
        self.assertEqual(s.read(), "{'id': 29, 'width': 10, 'height': 2, 'x': 1, 'y': 9}\n")
