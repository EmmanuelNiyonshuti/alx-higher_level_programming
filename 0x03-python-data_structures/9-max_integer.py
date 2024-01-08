#!/usr/bin/python3
"""Finds the biggest integer of a list"""


def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        for i in my_list:
            if my_list[i] > my_list[i + 1]:
                return my_list[i]
            i += 1
