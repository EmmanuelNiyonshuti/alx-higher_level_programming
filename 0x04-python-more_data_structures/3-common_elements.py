#!/usr/bin/python3
"""Returns a set of common elements in two sets."""


def common_elements(set_1, set_2):

    common_element = set()

    for element in set_1:
        if element in set_2:
            common_element.add(element)
    return common_element
