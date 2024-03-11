#!/usr/bin/python3
"""
Provides a function for converting custom object to json serializable.
"""


def class_to_json(obj):
    return vars(obj)
