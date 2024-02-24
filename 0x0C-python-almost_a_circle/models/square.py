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
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """string representation of the object"""
        return '[Square]({}) {}/{} - {}'.format(self.id, self.x, self.y, self.size)
