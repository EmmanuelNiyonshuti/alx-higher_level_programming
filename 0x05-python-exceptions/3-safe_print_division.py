#!/usr/bin/python3
"""divides 2 integers and prints the result."""


def safe_print_division(a, b):

    result = 0
    result = a / b
    try:
        return result

    except (ZeroDivisionError, TypeError):
        return None

    finally:
        print("Inside result:{}".format(result))
