#!/usr/bin/python3
"""
This module comprises a Mylist class.
"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """Prints sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
