#!/usr/bin/python3
"""comprise a function that perform file operations
"""

def append_write(filename="", text=""):
    """
    append_write -  appends a string at the end of a text file.

    args:
    - filename: The text file.
    - text: The string to append to the file.

    Return:
    Number of characters added.
    """

    with open(filename, "a", encoding="utf-8") as my_file:
        num_char = my_file.write(text)
        return num_char
