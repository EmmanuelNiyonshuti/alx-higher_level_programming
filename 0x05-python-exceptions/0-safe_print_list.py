#!/usr/bin/python3
"""safe_print_list - prints x elements of a list."""


def safe_print_list(my_list=[], x=0):

    num_elts = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            num_elts += 1
    except IndexError:
        pass

    finally:
        print()

    return num_elts
