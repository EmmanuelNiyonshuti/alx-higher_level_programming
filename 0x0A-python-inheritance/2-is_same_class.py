#!/usr/bin/python3
"""
This module comprises that checks
if an object is an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    - is_same_class - checks if an object is
    an instance of instance of a class.

    args:
    - obj: The object.
    - a_class: A class.

    Return:
    True  if the object is exactly an instance of the specified class.
    False otherwise.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
