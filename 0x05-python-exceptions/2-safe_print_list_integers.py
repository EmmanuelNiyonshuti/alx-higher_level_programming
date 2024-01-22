#!usr/bin/python3
"""Prints the first x elements of a list and only integers"""

def safe_print_list_integers(my_list=[], x=0):

    i = 0

    try:
        while i < x:
            value = my_list[i]

            if type(value) is int:
                print("{:d}".format(value), end="")
                i += 1
            else:
                raise ValueError

    except(ValueError, TypeError, IndexError):
        pass

    print()

    return i
