#!/usr/bin/python3
# 2-rectangle.py
# Rachid BOULMANI
"""Define a class Rectangle."""


class Rectangle:
    """
    a class Rectangle that defines a rectangle by:
    (based on 1-rectangle.py)
    Private instance attribute: width, must be an integer >= 0
    Private instance attribute: height, must be an integer >= 0
    """

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """property def width(self): to retrieve width"""
        return (self.__width)

    @property
    def height(self):
        """property def height(self): to retrieve height"""
        return (self.__height)

    @width.setter
    def width(self, value):
        """property setter def width(self, value): to set width
        with width must be an integer >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """property setter def height(self, value): to set height
        with height must be an integer >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method that
        returns the rectangle area
        """
        result = self.width * self.height
        return (result)

    def perimeter(self):
        """Public instance method that
        returns the rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return (0)
        else:
            result = 2 * (self.width + self.height)
            return (result)
