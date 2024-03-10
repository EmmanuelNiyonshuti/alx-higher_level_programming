#!/usr/bin/python3
"""This module contains a class Square"""


class Square:
    """defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        self._size = size
        self._position = position

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """Property to retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Property setter to set the position"""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        """ prints in stdout the square with the character '#'"""
        if self._size == 0:
            print()
        else:
            for _ in range(self._position[1]):
                print()
            for _ in range(self._size):
                print(" " * self._position[0] + "#" * self._size)
