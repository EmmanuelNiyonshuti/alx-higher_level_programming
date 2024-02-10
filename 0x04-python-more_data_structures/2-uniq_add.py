#!/usr/bin/python3
"""adds all unique integers in a list(only once for each integer)"""


def uniq_add(my_list=[]):

    unique_set = set(my_list)
    total = sum(unique_set)

    return total
