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
        """ retrieves a dictionary representation of a Student instance"""
        l_attr = list(attrs)
        for items in l_attr:
            if isinstance(items, str):
                return items
            else:
                return l_attr
        return self.__dict__
