#!/usr/bin/python3
"""Prints all integers of a list, in reverse order"""


def print_reversed_list_integer(my_list=[]):

    j = my_list.reverse()
    for j in my_list:
        print("{}".format(j))
