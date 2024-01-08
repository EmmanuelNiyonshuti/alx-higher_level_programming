#!/bin/usr/python3
"""finds all multiples of 2 in a list."""


def divisible_by_2(my_list=[]):

    new_list = []
    n = len(my_list)
    n_new = len(new_list)
    n_new = n

    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return new_list
