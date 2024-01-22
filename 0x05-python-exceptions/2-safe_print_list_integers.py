#!usr/bin/python3
"""Prints the first x elements of a list and only integers"""

def safe_print_list_integers(my_list=[], x=0):

    i = 0

    try:
        while i < x:
            value = my_list[i]

            if type(value) is not int:
                raise ValueError

            print("{:d}".format(value), end="")
            i += 1

    except(ValueError, TypeError, IndexError):
        pass

    finally:
        print()

    return i
