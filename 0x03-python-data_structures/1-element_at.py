#!/usr/bin/python3
"""retrieves an element from a list like in C."""


def element_at(my_list, idx):
    element = my_list[idx]
    n = len(my_list)

    for idx in my_list:
        if idx < 0:
            return None
        if idx > n:
            return None
        else:
            return element
