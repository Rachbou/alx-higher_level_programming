#!/usr/bin/python3
# 8-rectangle.py
# Rachid BOULMANI
"""
a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
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
