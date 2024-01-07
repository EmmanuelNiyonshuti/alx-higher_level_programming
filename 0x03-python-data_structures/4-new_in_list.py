#!/usr/bin/python3
"""replaces an element in a list"""


def new_in_list(my_list, idx, element):
    list = my_list[:]
    for i in my_list:
        if idx < 0 and idx > len(my_list):
            return list
        else:
            list[idx] = element
            return list
