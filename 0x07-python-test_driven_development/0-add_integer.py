#!/usr/bin/python3
"""This module comprises a function that adds integers.
"""


def add_integer(a, b=98):

    """Adds two integers
    Args:
    a: Integer or float
    b: Integer or float (default 98)

    raises:
    when a and b are not integers
    TypeError with a message a must be an integer or b must be an integer.

    return:
    sum of a and b

    return a + b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a + b)
