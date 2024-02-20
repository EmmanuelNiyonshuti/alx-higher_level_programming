#!/usr/bin/python3
"""
This Module to provide functionality for checking inheritance relationships.
"""
def inherits_from(obj, a_class):
    """
    Return True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.
        Args:
        - obj: An object to be checked.
        - a_class: A class to be checked against.

        Returns:
        True if obj is an instance of a subclass of a_class, otherwise False.
    """

    return isinstance(obj, a_class) and issubclass(type(obj), a_class)
