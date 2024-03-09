#!/usr/bin/python3
"""This module contains a function that adds attributes to object."""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if possible.
    Args:
        obj: The object to which the attribute will be added.
        attr_name: The name of the attribute.
        attr_value: The value of the attribute.
    Raises:
        TypeError: If the object cannot have a new attribute.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
