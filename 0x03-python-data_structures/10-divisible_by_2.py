#!/bin/usr/python3
"""finds all multiples of 2 in a list."""


def divisible_by_2(my_list=[]):

    new_list = []

    for num in my_list:

        is_divisible = num % 2 == 0

        new_list.append(is_divisible)

    return new_list
