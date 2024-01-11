#!/usr/bin/python3
"""adds all unique integers in a list(only once for each integer)"""


def uniq_add(my_list=[]):

    unique_set = set()
    total = 0

    for num in my_list:
        if num not in unique_set:
            total += num
            unique_set.add(num)

    return total
