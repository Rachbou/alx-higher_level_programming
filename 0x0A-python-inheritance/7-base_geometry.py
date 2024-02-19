#!/usr/bin/python3
# 7-base_geometry.py
# Rachid BOULMANI
"""
a class BaseGeometry (based on 6-base_geometry.py)
"""


class BaseGeometry:
    """
    Class BaseGeometry (based on 5-base_geometry.py) Public instance method:
    area(): that raises an Exception with the message:
        area() is not implemented
    integer_validator(name, value): that validates that value is an integer
    and is greater than 0.
    """

    def area(self):
        """
        Raises
        ------
        Exception: area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Raises
        ------
        TypeError: <name> must be an integer:
            if value is not an integer
        ValueError: <name> must be greater than 0:
            if value is less or equal to 0.
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
