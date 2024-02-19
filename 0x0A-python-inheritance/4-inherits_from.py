#!/usr/bin/python3
# 4-inherits_from.py
# Rachid BOULMANI
"""
Function that test if an object is an instance of a class that inherited
(directly or indirectly) a specified class
"""


def inherits_from(obj, a_class):
    """
    a function that returns:
        True: if the object is an instance of a class that inherited
        (directly or indirectly) the specified class
        False: otherwise.
    """

    if type(obj) is a_class:
        return (False)
    return (isinstance(obj, a_class))
