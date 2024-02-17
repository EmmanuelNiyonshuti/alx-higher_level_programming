#!/usr/bin/python3
"""
This module comprises a function that prints name.
"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>
    args:
    first_name: string.
    last_name: string.
    Return:
    Nothing
    raise:
    TypeError when first_name or last_name is not a string.
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
