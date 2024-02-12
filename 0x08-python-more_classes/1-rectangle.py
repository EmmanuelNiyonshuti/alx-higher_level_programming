#!/usr/bin/python3
"""This module comprises a class that defines a Rectangle"""


class Rectangle:
    """Defines a Rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieving width"""
        self.__width

    @width.setter
    def width(self, value):
        """Property setter to set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieving height"""
        self.__height

    @height.setter
    def height(self, value):
        """Property setter to set Height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
