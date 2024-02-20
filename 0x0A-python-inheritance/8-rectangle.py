#!/usr/bin/python3
"""
comprises Rectangle class that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """My Rectangle class"""
    def __init__(self, width, height):
        """Instantiation"""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
