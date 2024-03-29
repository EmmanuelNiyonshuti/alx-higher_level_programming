#!/usr/bin/python3

"""Square Module: Contains the Square class"""


class Square:
    """class Square that defines a square """
    def __init__(self, size=0):
        """Instantiation with optional size: def __init__(self, size=0)"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
