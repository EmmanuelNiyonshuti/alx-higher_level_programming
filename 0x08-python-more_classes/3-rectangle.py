#!/usr/bin/python3
"""This module comprises a class of Rectangle"""


class Rectangle:
    """Defines a Rectangle"""

    def __init__(self, width=0, height=0):
        """Instantion with width and height"""
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
        """Return the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):

        """"Return the rectangle parameter"""
        if self.__height == 0:
            return 0
        if self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    @property
    def width(self):
        """Retrieving width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """Return a string representantion of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""

        rectangle_str = ""

        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"

        return rectangle_str[:-1]
