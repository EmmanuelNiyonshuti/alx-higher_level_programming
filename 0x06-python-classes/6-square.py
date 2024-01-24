#!/usr/bin/python3
"""Square Module: Contains the Square class"""


class Square:
    """Square class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size and optional position"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        if not isinstance(position, tuple) or len(position) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Property to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter to set the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

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

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Public instance method that prints the square with #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
