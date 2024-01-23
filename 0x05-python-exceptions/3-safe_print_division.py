#!/usr/bin/python3
"""divides 2 integers and prints the result."""


def safe_print_division(a, b):

    result = None
    try:
        result = a / b

        return result

    except ZeroDivisionError:
        return None

    finally:
        print("Inside result:{}".format(result))
