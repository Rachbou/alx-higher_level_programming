#!/usr/bin/python3
# 3-is_kind_of_class.py
# Rachid BOULMANI
"""
Function that tests if an object is an instance of a specified class,
or if its an instance of a class that inherited from the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    a function that returns:
        True: if the object is an instance of the specified class or if its
        an instance of a class that inherited from the specified class
        False: otherwise.
    """

    return (isinstance(obj, a_class))
