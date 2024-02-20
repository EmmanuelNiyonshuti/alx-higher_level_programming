#!/usr/bin/python3
"""This module comprises a class defined based on 5-base_geometry.py"""

class BaseGeometry:
    """My BaseGeometry class"""

    def area(self):
        """
        Compute the area of the geometry shape.

        Raises:
            NotImplementedError: If the area computation is not implemented for the shape.
        """
        raise NotImplementedError("area() is not implemented")
