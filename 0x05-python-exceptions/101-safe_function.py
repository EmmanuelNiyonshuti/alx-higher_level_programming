#!/usr/bin/python3
"""
This module contains a function that executes a another function
safely.
"""
import sys


def safe_function(fct, *args):
    """
    Executes a function safely.

    Args:
        fct: A pointer to the function to be executed.
        *args: Arbitrary positional arguments to be passed to the function.

    Returns:
    The result of the function execution, or None if an exception occurs.

    If an exception occurs during the execution of the function, it is caught
    and the exception message is printed to stderr. The function returns None
    in this case.
    """

    try:
        return fct(*args)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None
