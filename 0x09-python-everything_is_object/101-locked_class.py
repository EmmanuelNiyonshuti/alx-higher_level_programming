#!/usr/bin/python3
"""This module comprises a class
that defines with restricted set of allowed attributes"""

def LockedClass:
    """Defines a a restricted set of attributes"""
    __slots__ = ["first_name"] """Instances of the LockedClass
    can only have one attribute 'first_name'"""

    def __setattr__(self, name, value):
        """Called whenever an attempt is made
        to set an attribute on an instance of the class"""
        if name != "first_name":
            raise AttributeError("LockedClass has no attribute '{}'".format(name))
        super().__setattr__(name, value):
            """ If the attribute being set is first_name, this line calls
            the superclass's __setattr__ method 
            to actually set the attribute on the instance"""
