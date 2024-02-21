#!/usr/bin/python3
"""
This module provides functions for working with JSON data
and text files.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - writes an Object to a text file,
                        using a JSON representation.
    args:
    - my_obj: The object to write to a file.
    - filename: The file to write to.
    Return:
    Nothing.
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)
