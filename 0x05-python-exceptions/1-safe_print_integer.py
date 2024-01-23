#!/usr/bin/python3
"""Prints an integer with "{:d}".format()"""


def safe_print_integer(value):

    try:
        a = int(value)
        print("{:d}".format(a))
        return True
    except:
        pass
    else:
        return False
