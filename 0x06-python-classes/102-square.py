#!/usr/bin/python3
"""Square Module: Contains the Square class"""

"""from functools import total_ordering
@total_ordering"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        """Instantiation with optional size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size

    def area(self):
        """Public instance method that returns the current square area"""
        return self._size * self._size

    @property
    def size(self):
        """Getter method to retrieve the value of size"""

        return self._size

    @size.setter
    def size(self, value):
        """Setter method to set the value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Overriding operators"""
    def __eq__(self, other):
        return self._size == other

    def __ne__(self, other):
        return self._size != other

    def __gt__(self, other):
        return self._size > other

    def __ge__(self, other):
        return self._size >= other

    def __lt__(self, other):
        return self._size < other

    def __le__(self, other):
        return self._size <= other
