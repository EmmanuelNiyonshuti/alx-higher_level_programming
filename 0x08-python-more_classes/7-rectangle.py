#!/usr/bin/python3
"""This module comprises a class that defines a Rectangle"""


class Rectangle:
    """Defines a Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
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
        Rectangle.number_of_instances += 1

    def area(self):
        """Returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the rectangle parameter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        Rectangle_str = ""
        for _ in range(self.__height):
            Rectangle_str += Rectangle.print_symbol * self.__width + "\n"
        return Rectangle_str.strip()

    def __repr__(self):
        """Returns a string Representation of the rectangle"""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Retrieving width"""
        return self.__width

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
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
