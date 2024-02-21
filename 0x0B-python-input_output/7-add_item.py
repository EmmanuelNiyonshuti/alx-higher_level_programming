#!/usr/bin/python3
"""
This module provides functions for working with JSON data and text files.
"""
import sys
from os import path
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

"""Checking is a file exist and create an empty list if not"""
if not path.exists("add_item.json"):
    save_to_json_file([], "add_item.json")

"""Loading existing data from add_item.json"""
data = load_from_json_file("add_item.json")

"""Add command line arguments to the list"""
for args in sys.argv[1:]:
    data.append(args)

"""Save the updated list to add_item.json"""
save_to_json_file(data, "add_item.json")
