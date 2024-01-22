#!/usr/bin/python3
"""safe_print_list - prints x elements of a list."""


def safe_print_list(my_list=[], x=0):

    i = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
    except:
        pass

    print()

    return i
