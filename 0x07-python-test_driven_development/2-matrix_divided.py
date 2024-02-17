#!/usr/bin/python3
"""
This module comprises a function that divides elements of the matrix.
"""


def matrix_divided(matrix, div):
    """Divides a matrix
    args:
    @matrix: a list of list of integers or floats.
    @div: number to divide the matrix with.

    Return:
    a new matrix.
    """

    row_len = len(matrix[0])
    for row in matrix:
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    new_matrix = [[]]

    new_matrix = [[round(x/div, 2) for x in row] for row in matrix]

    return new_matrix
