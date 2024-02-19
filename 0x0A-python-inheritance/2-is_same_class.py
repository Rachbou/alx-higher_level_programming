#!/usr/bin/python3
# 2-is_same_class.py
# Rachid BOULMANI
"""
Function that tests if the object is exactly an instance of a specified class
"""


def is_same_class(obj, a_class):
    """
    a function that returns:
        True: if the object is exactly an instance of the specified class
        False: otherwise.
    """

    if type(obj) == a_class:
        return (True)
    return (False)
