#!usr/bin/python3
"""Prints the first x elements of a list and only integers"""

def safe_print_list_integers(my_list=[], x=0):

    try:
        for i in range(x):
            value = int(my_list[i])
            print("{:d}".format(value), end='')
            i += 1
    except IndexError:
        pass
    print()

    return i
