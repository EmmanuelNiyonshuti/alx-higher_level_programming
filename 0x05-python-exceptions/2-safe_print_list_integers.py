#!usr/bin/python3
"""Prints the first x elements of a list and only integers"""

def safe_print_list_integers(my_list=[], x=0):

    num_printed = 0
    try:
        for i, value in enumerate(x):
            if num_printed < x and isinstance(value, int):
                print(":d}".format(value), end="")
                num_printed += 1
        print()
    except (ValueError, TypeError, IndexError):
        pass
    return num_printed
