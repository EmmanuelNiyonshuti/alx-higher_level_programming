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
        """
        Validate an integer value.

        This method validates the input value to ensure it is an integer
        and greater than zero.

        Parameters:
        - name (str): The name of the value being validated.
        - value (int): The value to be validated.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is not greater than zero.

        Returns:
        - str: The validated name.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return name
