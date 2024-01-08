#!/usr/bin/python3
"""Finds the biggest integer of a list"""


def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        n = len(my_list)
        for i in range(n):
            for j in range(0, n-i-1):
                if my_list[j] > my_list[j + 1]:
                    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
            return (my_list[- 1])
