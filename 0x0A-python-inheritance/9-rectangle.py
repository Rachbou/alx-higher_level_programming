#!/usr/bin/python3
# 9-rectangle.py
# Rachid BOULMANI
"""
a class Rectangle that inherits from BaseGeometry (8-rectangle.py).
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
    with private width and height that must be positive integers
    """

    def __init__(self, width, height):
        """Instantiation with width and height:
        width and height must be private. No getter or setter
        width and height must be positive integers,
        validated by integer_validator
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Returns
        -------
        area : Integer
            The area of the rectangle.
        """
        area = self.__width * self.__height
        return (area)

    def __str__(self):
        """
        str representation of Rectangle [Rectangle] <width>/<height>
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
