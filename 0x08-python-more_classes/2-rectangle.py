#!/usr/bin/python3
"""This module comprises a class that defines a Rectangle"""


class Rectangle:
    """defines a Rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiation with width and height"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the ractangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        if self.__height or self.__width == 0:
            return 0

        return 2 * (self.__height + self.__width)

    @property
    def width(self):
        """Retrieving the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieving height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
