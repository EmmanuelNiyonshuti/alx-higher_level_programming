#!/usr/bin/python3
"""
This module comprises a function that
checks  if the object is an instance of, or
if the object is an instance of a class that inherited from.
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class - checks the object's instance.

    args:
    - obj: object.
    - a_class: class.

    Return:
    True if the object is an instance of the specified class or subclass.
    Otherwise False.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
