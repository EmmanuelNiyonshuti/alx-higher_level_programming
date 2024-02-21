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
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings,
        only attribute names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved.
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict
        return {attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)}
