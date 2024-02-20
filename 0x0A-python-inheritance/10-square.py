#!/usr/bin/python3
"""
This module comprises a class that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ My Square Class"""
    def __init__(self, size):
        """Instantiation"""
        super().__init__(size, size)
