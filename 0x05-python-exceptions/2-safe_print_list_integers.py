#!usr/bin/python3
"""Prints the first x elements of a list and only integers"""


def safe_print_list_integers(my_list=[], x=0):

    num_printed = 0
    i = 0

    try:
        while num_printed < x:
            value = my_list[i]

            if isinstance(value, int):
                print("{:d}".format(value), end="")
                num_printed += 1

            i += 1
    except IndexError:
        pass
    print()
    return num_printed
