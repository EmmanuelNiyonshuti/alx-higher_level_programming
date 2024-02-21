#!/usr/bin/python3
"""
comprises a student class.
"""


class Student:
    """My student class"""
    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns a dictionary representation of the instance,
        with the option to include only specific attributes
        if a list of attribute names is provided.
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__

        return {attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
