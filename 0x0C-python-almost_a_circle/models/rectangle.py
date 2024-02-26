#!/usr/bin/python3
"""
This module provides class that inherits from another class.
"""
from .base import Base


class Rectangle(Base):
    """Inherits from Base base class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiating"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
        if type(width) != int:
            raise TypeError("width must be an integer")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if type(x) != int:
            raise TypeError("x must be an integer")
        if type(y) != int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

    """managing attributes"""
    @property
    def width(self):
        """Retrieving width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieving height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the value"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieving x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting the value"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieving y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting the value"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of a rectangle"""
        return self.height * self.width

    def display(self):
        """prints string representation of object as '#'"""
        rect = ""
        print("\n" * self.__y, end="")
        for _ in range(self.__height):
            rect += (" " * self.__x) + ("#" * self.__width) + "\n"
        print(rect, end="")

    def __str__(self):
        """Prints string representation of the object"""
        return f'[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}'

    def update(self, *args, **kwargs):
        """assigns positional arguments to each attribute.
            args:
            - args: no-keyword argument.
            -kwargs: key-worded argument.
        """
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

        if not len(args):
            for key, value in kwargs.items():
                setattr(self, key, value)
                """self.__setattr__(key, value)"""

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
