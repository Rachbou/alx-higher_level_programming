#!/usr/bin/python3
# square.py
# Rachid BOULMANI
"""
the class 'Square' that inherits from the class 'Rectangle'.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square with:
        inheriting from the class 'Rectangle'
        overriding the __str__ method
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        class constructor:
            Call the super class with id, x, y, width and height
            width = height = size
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of a Square"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))
