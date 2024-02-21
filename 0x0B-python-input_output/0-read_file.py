#!/usr/bin/python3
"""This module comprises a function that reads a text file"""


def read_file(filename=""):
    """
    read_file - reads a text file and print it to stdout.

    args:
    -filename: a file to be read.
    Return:
    Nothing.
    """

    with open(filename, encoding="utf-8") as a_file:
        for line in a_file:
            print(line, end='')
