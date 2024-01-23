#!/usr/bin/python3
"""divides 2 integers and prints the result."""


def safe_print_division(a, b):

    try:
        return a / b
    except ZeroDivisionError:
        return None

    finally:
        print("Inside result:{}".format(result))
