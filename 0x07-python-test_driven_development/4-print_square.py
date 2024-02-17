#!/usr/bin/python3
"""
This module comprises a function that prints a square.
"""

def print_square(size):
    """Prints a square with the character '#'.

    args:
    size: size length of the square.

    Return:
    Nothing.

    raises:
    TypeError when size is not an integer
    ValueError when size id less than zero
    TypeError when size is a float and is less than 0
    """

    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")

    for i in range(size):
        print('#' * size)
