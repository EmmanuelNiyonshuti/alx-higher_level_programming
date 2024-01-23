#!usr/bin/python3
"""Prints the first x elements of a list and only integers"""

def safe_print_list_integers(my_list=[], x=0):

    try:
        num_printed = 0
        for i in range(0, x):

            int(my_list[i])

            print("{:d}".format(my_list[i]), end="")

            num_printed += 1
        print()

    except (IndexError, TypeError):
        pass

    return num_printed
