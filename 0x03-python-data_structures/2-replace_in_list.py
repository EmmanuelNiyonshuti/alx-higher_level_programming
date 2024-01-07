#!/usr/bin/python3
"""replaces an element of a list at a specific position (like in C)"""


def replace_in_list(my_list, idx, element):
    for i in my_list:
        if i < 0:
            return my_list
        elif i > len(my_list):
            return my_list
        else:
            my_list[idx] = element
