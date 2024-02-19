#!/usr/bin/python3
# 0-lookup.py
# Rachid BOULMANI
"""
a function that returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """returns the list of available attributes and methods of an object
    args:
        obj : object to lookup
    """

    return (dir(obj))
