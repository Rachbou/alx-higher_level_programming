#!/usr/bin/python3
# 2-square.py
# Rachid BOULMANI
"""Define a class Square."""


class Square:
    """
    class Square that defines a square by:
    (based on 1-square.py)
    """

    def __init__(self, size=0):
        """Instantiation with optional size
        with size must be an integer >= 0
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
