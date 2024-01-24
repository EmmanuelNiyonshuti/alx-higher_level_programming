#!/usr/bin/python3

"""Square Module: Contains the Square class"""


class Square:

    """class Square that defines a square by Private instance attribute: size"""

    def __init__(self, size):

        """Instantiation with size (no type/value verification)"""
        self.__size = size
