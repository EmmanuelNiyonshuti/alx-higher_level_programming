#!/usr/bin/python3
"""Prints a matrix of integers"""


def print_matrix_integer(matrix=[[]]):
    num_rows = len(matrix)
    num_columns = len(matrix[0]) if matrix and matrix[0] else 0

    for i in range(num_rows):
        for j in range(num_columns):
            print("{:d}".format(matrix[i][j]), end=" " if j < num_columns - 1 else "")
        print()
