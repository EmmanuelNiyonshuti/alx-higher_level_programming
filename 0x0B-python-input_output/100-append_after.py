#!/usr/bin/python3
"""
This module provides a function for working with files.
"""

def append_after(filename="", search_string="", new_string=""):
    """
    append_after -  inserts a line of text to a file,
                    after each line containing a specific string.
    args:
    - filename: The name of the file.
    - search_string: string in a file.
    - new_string: string to be appended.
    Return:
    The appended file.
    """
    with open(filename, "a+", encoding="utf-8") as my_file:
        contents = my_file.read()
        if search_string in contents:
            my_file.write(new_string)
