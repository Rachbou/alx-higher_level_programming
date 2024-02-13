#!/usr/bin/python3
# FileName.py
# Rachid BOULMANI
"""a function that multiplies 2 matrices
args:
    m_a : must be an list of lists of integers or floats
    m_b : must be an list of lists of integers or floats
m_a and m_b must be validated before been multiplied.
"""


def matrix_mul(m_a, m_b):
    """
    a function that multiplies 2 matrices
    """

    # Validating that m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    # Validating that m_a and m_b are lists of lists
    if not all(isinstance(el, list) for el in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(el, list) for el in m_b):
        raise TypeError("m_b must be a list of lists")
    # Validating that m_a and m_b are not empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    # Validating that all elements of the matrices are integers or a floats
    if not all(all(isinstance(el, (int, float)) for el in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not all(all(isinstance(el, (int, float)) for el in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")
    # Validating that m_a and m_b are a rectangle
    if any(len(el) != len(m_a[0]) for el in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(el) != len(m_b[0]) for el in m_b):
        raise TypeError("each row of m_b must be of the same size")
    # Validating that m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    rows = len(m_a)
    colms = len(m_b[0])
    new_matrice = []
    for i in range(rows):
        new_row = []
        for j in range(colms):
            result = 0
            for k in range(len(m_b)):
                result += m_a[i][k] * m_b[k][j]
            new_row.append(result)
        new_matrice.append(new_row)
    return (new_matrice)
