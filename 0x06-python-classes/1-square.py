#!/usr/bin/python3
# 1-square.py
# Rachid BOULMANI
"""Define a class Square."""


class Square:
    """
    a class Square that defines a square by: (based on 0-square.py)
    Private instance attribute: size
    """

    def __init__(self, size):
        """Instantiation with size (no type/value verification)"""
        self.__size = size
