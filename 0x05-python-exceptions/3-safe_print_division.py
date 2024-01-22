#!/usr/bin/python3
"""divides 2 integers and prints the result."""


def safe_print_division(a, b):

    try:
        value = a / b
    except ZeroDivisionError:
        value = None
    finally:
        print("Inside Result: {}".format(value))
    return value
