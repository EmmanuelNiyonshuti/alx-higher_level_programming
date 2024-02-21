#!/usr/bin/python3
"""
This module provides functions for working with JSON data and text files.
"""

import json

def load_from_json_file(filename):
    """
    load_from_json_file - creates an Object from a “JSON file.
    args:
    filename: The object file.
    Return:
    Nothing.
    """
    with open(filename, "r", encoding="utf-8") as my_file:
        return json.load(my_file)
