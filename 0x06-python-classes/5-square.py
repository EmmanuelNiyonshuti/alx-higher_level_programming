#!/usr/bin/python3
"""Square Module: Contains the Square class"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        """Instantiation with optional size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Public instance method that prints the square with #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
