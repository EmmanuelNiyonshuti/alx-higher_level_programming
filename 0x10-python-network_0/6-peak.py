#!/usr/bin/python3
"""
comprise a find_peak algorithm
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    n = len(list_of_integers)
    for i in range(n):
        left = i - 1
        right = i + 1
        if left > - 1 and right < n:
            if list_of_integers[i] >= list_of_integers[left] and list_of_integers[i] >= list_of_integers[right]:
                return list_of_integers[i]
        elif left == -1:
            if list_of_integers[i] >= list_of_integers[right]:
                return list_of_integers[i]
        elif right == n:
            if list_of_integers[i] >= list_of_integers[left]:
                return list_of_integers[i]