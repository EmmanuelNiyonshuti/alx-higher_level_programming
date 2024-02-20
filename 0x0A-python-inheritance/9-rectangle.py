#!/usr/bin/python3
"""
This module Comprises a class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """My Rectangle class"""
    def __init__(self, width, height):
        """Instantiation"""
        validated_width = self.integer_validator("width", width)
        validated_height = self.integer_validator("height", height)
        self.__width = validated_width
        self.__height = validated_height

    def area(self):
        """Area of a Rectangle"""
        return self.__height * self.__width

    def __str__(self):
        return "[{}] {} / {}".format(type(self).__name__, self.__width, self.__height)
