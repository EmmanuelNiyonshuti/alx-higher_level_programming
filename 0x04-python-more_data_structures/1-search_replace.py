#!/usr/bin/python3
"""replaces all occurrences of an element by another in a new list."""


def search_replace(my_list, search, replace):

    new_list = [replace if x == search else x for x in my_list]

    return new_list
