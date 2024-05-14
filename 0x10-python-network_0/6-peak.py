#!/usr/bin/python3
"""
comprise a find_peak algorithm
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    peak is a number which is greater than or equal to it's neighbours.
    this function starts from 0 of the list,
    compare each current number to it's neighbours
    and then returns peak whenever it encounters it.
    """
    n = len(list_of_integers)
    peak = None
    for i in range(1, n - 1):
        left = i - 1
        right = i + 1
        if (list_of_integers[i] >= list_of_integers[left] and list_of_integers[i] >= list_of_integers[right]):
            peak = list_of_integers[i]
    return peak
