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
    lines = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)