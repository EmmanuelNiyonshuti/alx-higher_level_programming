#!/usr/bin/python3
"""replaces an element of a list at a specific position (like in C)"""


def replace_in_list(my_list, idx, element):
    l = len(my_list)
    while my_list[idx]:
        if my_list[idx] < 0:
            return my_list
        elif my_list[idx] > l:
            return my_list
        else:
            my_list[idx] = element
