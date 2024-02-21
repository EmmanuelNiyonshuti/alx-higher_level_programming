#!/usr/bin/python3
"""
This module Contains a function that represents Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    pascal_triangle: Represents a pascal's triangle.
    args:
    - n: Size of the Rectangle.
    Return:
    returns a list of lists of integers.
    """

    if n <= 0:
        return []

    p_triangle = [[1]]

    for i in range(1, n):
        prev = p_triangle[-1]
        next_row = [1]
        for j in range(1, len(prev)):
            next_row.append(prev[j - 1] + prev[j])
        next_row.append(1)
        p_triangle.append(next_row)

    return p_triangle
