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

    json_str = json.dumps(my_obj)

    return json_str

