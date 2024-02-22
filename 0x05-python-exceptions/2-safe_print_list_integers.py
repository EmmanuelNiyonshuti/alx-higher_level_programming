#!/usr/bin/python3
"""Prints the first x elements of a list and only integers"""


def safe_print_list_integers(my_list=[], x=0):

    num = 0
    for i in range(x):
        try:
            j = int(i)
            print("{:d}".format(my_list[j]), end='')
            num += 1
        except (TypeError, ValueError):
            pass
    print()
    return num
