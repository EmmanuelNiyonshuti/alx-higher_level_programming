#!usr/bin/python3
"""Prints the first x elements of a list and only integers"""


def safe_print_list_integers(my_list=[], x=0):

    num = 0
    try:
        for i in range(x):
            j = int(i)
            print("{:d}".format(my_list[j]), end='')
        return num
    except (TypeError, ValueError):
        pass
    print()
