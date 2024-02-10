#!/usr/bin/python3
# 2-matrix_divided.py
# Rachid BOULMANI
"""function that divides all elements of a matrix.
args :
    matrix : must be a list of lists of integers or floats
    and each row of the matrix must be of the same size.
    div : must be a number (integer or float).
"""


def matrix_divided(matrix, div):
    """
    a function that divides all elements of a matrix.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_size = 0
    if len(matrix) > 0:
        row_size = len(matrix[0])

    new_matrix = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
            new_element = round(element / div, 2)
            new_row.append(new_element)
        new_matrix.append(new_row)
    return (new_matrix)
