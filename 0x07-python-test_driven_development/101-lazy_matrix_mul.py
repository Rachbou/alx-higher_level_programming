#!/usr/bin/python3
# 101-lazy_matrix_mul.py
# Rachid BOULMANI
"""a function that multiplies 2 matrices
args:
    m_a : must be an list of lists of integers or floats
    m_b : must be an list of lists of integers or floats
"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    a function that multiplies 2 matrices
    using the module NumPy
    """

    new_matrice = numpy.matmul(m_a, m_b)
    return (new_matrice)
