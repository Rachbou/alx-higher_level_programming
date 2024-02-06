#!/usr/bin/python3
# 4-square.py
# Rachid BOULMANI
"""Define a class Square."""


class Square:
    """
    class Square that defines a square by:
    (based on 3-square.py)
    """

    def __init__(self, size=0):
        """Instantiation with optional size"""
        self.size = size

    @property
    def size(self):
        """property def size(self): to retrieve size"""
        return(self.__size)

    @size.setter
    def size(self, size):
        """property setter def size(self, value): to set size
        with size must be an integer >= 0
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Public instance method: def area(self):
        that returns the current square area
        """
        return (self.__size ** 2)
