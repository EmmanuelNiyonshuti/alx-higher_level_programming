#!/usr/bin/python3
""" prints a matrix of integers"""


def print_matrix_integer(matrix=[[]]):
    num_rows = len(matrix)
    num_columns = len(matrix[0] if matrix else 0)
    for i in range(num_rows):
        for j in range(num_columns):
            print("{:d}".format(matrix[i][j]), end =" ")
        print()
