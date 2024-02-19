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
        Exception
            area() is not implemented.

        Returns
        -------
        None.

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Parameters
        ----------
        name : String
        value : Integer

        Raises
        ------
        TypeError
            <name> must be an integer.
        ValueError
            <name> must be greater than 0.

        Returns
        -------
        None.

        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
