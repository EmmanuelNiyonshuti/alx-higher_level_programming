#!/usr/bin/python3


def add_integer(a, b=98):

    """

    This function adds two integers and/or float numbers
    Adds two integers.

    Args:
    a (int): First integer
    b (int): Second integer (default is 98).


    Returns:
    int: Sum of the two integers.

    Raises:
        typeError: If either 'a' or 'b' is not an integer or float.

    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

        a = int(a)
        b = int(b)

    return a + b
