#!/usr/bin/python3
# 0-add_integer.py
# Rachid BOULMANI
"""
a function that adds 2 integers.
"""


def add_integer(a, b=98):
    """add_integer function that adds 2 integers.
    args :
        a : Must be an integer.
        b : Must be an integer, but Optional (98)
    """
    
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    (a, b) = (int(a), int(b))
    return (a + b)
