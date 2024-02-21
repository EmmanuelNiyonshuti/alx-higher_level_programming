#!/user/bin/python3
"""
This module comprises a function
That returns a json string.
"""
import json


def to_json_string(my_obj):
    """
    to_json_string - gives a JSON string.

    args:
    - my_obj: Python object.
    Return:
    JSON representation of an object (string).
    """

    return json.dumps(my_obj, sort_keys=True)
