#!/usr/bin/python3
"""Prints all integers of a list, in reverse order"""


def print_reversed_list_integer(my_list=[]):
    i = len(my_list) - 1
    while i >= 0:
        print("{}".format(my_list[i]))
        i -= 1
