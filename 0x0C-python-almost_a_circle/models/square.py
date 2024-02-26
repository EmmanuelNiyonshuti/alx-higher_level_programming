#!/usr/bin/python3
"""
This module comprises class that inherits from another class
which is also a child class of the parent class.
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """Inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation"""
        Rectangle.__init__(self, size, size, x, y, id)
        self.size = size

    """overridding public instance method from Rectangle"""
    @property
    def width(self):
        """Retrieving size of the square"""
        return self.size

    @width.setter
    def width(self, value):
        """validating size of the square"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.size = value

    def __str__(self):
        """string representation of the square"""
        return '[Square]({}) {}/{} - {}'.format(self.id, self.x,
                                                self.y, self.size)

    def update(self, *args, **kwargs):
        """
        - update: assigns attributes.
        args:
        - args: non-key worded arguments.
        - kwargs:  key worded arguments.
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }