#!/usr/bin/python3
"""This module comprises a class defined based on 5-base_geometry.py"""


class BaseGeometry:
    """My BaseGeometry class"""

    def area(self):
        """
    area - Compute the area of the geometry shape.
    Raises:
        Exception: If the area computation is not implemented for the shape.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
