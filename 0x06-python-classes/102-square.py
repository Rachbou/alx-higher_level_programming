#!/usr/bin/python3
# 102-square.py
# Rachid BOULMANI
"""Define a class Square."""


class Square:
    """
    class Square that defines a square by:
    (based on 4-square.py)
    """

    def __init__(self, size=0):
        """Instantiation with optional size"""
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square"""
        return(self.__size)

    @size.setter
    def size(self, size):
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

    def __eq__(self, OtherSquare):
        """Define the == comparision."""
        return self.area() == OtherSquare.area()

    def __ne__(self, OtherSquare):
        """Define the != comparison."""
        return self.area() != OtherSquare.area()

    def __lt__(self, OtherSquare):
        """Define the < comparison."""
        return self.area() < OtherSquare.area()

    def __le__(self, OtherSquare):
        """Define the <= comparison."""
        return self.area() <= OtherSquare.area()

    def __gt__(self, OtherSquare):
        """Define the > comparison."""
        return self.area() > OtherSquare.area()

    def __ge__(self, OtherSquare):
        """Define the >= compmarison."""
        return self.area() >= OtherSquare.area()
