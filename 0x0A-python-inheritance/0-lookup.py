#!/usr/bin/python3
"""
This module comprises a function
that returns list of available attributes
and methods of object.
"""


def lookup(obj):
    """
    args:
    - obj: The object.

    Return:
    list of available attributes and methods.
    """
    return dir(obj)
