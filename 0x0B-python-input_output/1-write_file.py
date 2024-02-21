#!/usr/bin/python3
"""
this module comprise a function that writes to a file.
"""

def write_file(filename="", text=""):
    """
    write_file - writes a string to a text file.

    args:
    - filename: file to write to.
    - text: the string to write.

    Return:
    returns the number of characters written/
    """

    with open(filename, "w", encoding="utf-8") as my_file:
        num_char = my_file.write(text)
        return num_char
