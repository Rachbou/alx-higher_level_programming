#!/usr/bin/python3
# 10-square.py
# Rachid BOULMANI
"""
a class Square that inherits from Rectangle (9-rectangle.py).
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    a class Square that inherits from Rectangle (9-rectangle.py).
    with private size that must be positive integers
    """

    def __init__(self, size):
        """Instantiation with width and height:
        width and height must be private. No getter or setter
        width and height must be positive integers,
        validated by integer_validator
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
