#!/usr/bin/python3
"""
This module comprises a function
multiplies 2 matrices.
"""

def matrix_mul(m_a, m_b):
    """Multiplies two matrices
    args:
    -m_a: list of list of integers or floats.
    -m_b: list of list of integers or floats.

    Return:
    Nothing

    raises:
    TypeError if m_a or m_b is not a list. 
                m_a must be a list of lists or m_b must be a list of lists.
                if one element of those list of lists is not an integer or a float.
                if m_a or m_b is not a rectangle (all ‘rows’ should be of the same size)
    ValueError if m_a or m_b is empty (it means: = [] or = [[]]).
                m_a and m_b can't be multiplied.
    """

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
    
