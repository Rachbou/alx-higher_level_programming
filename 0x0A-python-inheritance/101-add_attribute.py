#!/usr/bin/python3
# 101-add_attribute.py
# Rachid BOULMANI
"""
a function that adds a new attribute to an object if it’s possible
"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it’s possible

    Parameters
    ----------
    obj : Object to add attribute to.
    name : The attribute to add to the object.
    value : The value of the attribute to add to the object.

    Raises
    ------
    TypeError: can't add new attribute
        if the object can’t have new attribute.

    Returns
    -------
    None.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
