#!/usr/bin/python3
"""Prints an integer with "{:d}".format()"""


def safe_print_integer(value):

    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        pass
    else:
        return True
