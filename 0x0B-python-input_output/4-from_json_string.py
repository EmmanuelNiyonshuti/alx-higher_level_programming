#!/usr/bin/python3
"""
This module contains a function that deserialize
deserialize JSON string.
"""
import json


def from_json_string(my_str):
    """deserializes json string.
    args:
    - my_str: json string.
    Return:
    an object (Python data structure) represented by a JSON string.
    """
    return json.loads(my_str)
