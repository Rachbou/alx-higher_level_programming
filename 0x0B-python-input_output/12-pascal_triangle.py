#!/usr/bin/python3
# 12-pascal_triangle.py
# Rachid BOULMANI
"""
a function that returns a list of lists of integers representing
the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    a function that returns a list of lists of integers representing
    the Pascal’s triangle of n
    """

    if n <= 0:
        return ([])

    triangle = [[1]]
    while len(triangle) != n:
        last = triangle[-1]
        row = [1]
        for i in range(1, len(last)):
            row.append(last[i - 1] + last[i])
        row.append(1)
        triangle.append(row)
    return (triangle)
