#!/usr/bin/python3
# 6-square.py
# Rachid BOULMANI
"""Define a class Square."""


class Square:
    """
    class Square that defines a square by:
    (based on 5-square.py)
    """

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size and optional position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """property def size(self): to retrieve size"""
        return(self.__size)

    @property
    def position(self):
        """property def position(self): to retrieve position"""
        return(self.__position)

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

    @position.setter
    def position(self, position):
        """property setter def position(self, value): to set position
        with position must be a tuple of 2 positive integers
        """
        if isinstance(position[0], int) and isinstance(position[1], int):
            if position[0] < 0 or position[1] < 0:
                raise TypeError("position must be a tuple \
                                of 2 positive integers")
            self.__position = position
        else:
            raise TypeError("position must be a tuple \
                            of 2 positive integers")

    def area(self):
        """Public instance method: def area(self):
        that returns the current square area
        """
        return (self.__size ** 2)

    def my_print(self):
        """Public instance method: def my_print(self):
        that prints in stdout the square with the character #
        if size is equal to 0, print an empty line
        position should be use by using space
        Don’t fill lines by spaces when position[1] > 0
        """
        if self.size == 0:
            print()
        else:
            if self.position[1] > 0:
                for i in range(self.position[1]):
                    print()
            for i in range(self.size):
                for j in range(self.size + self.position[0]):
                    if j < self.position[0]:
                        print(" ", end='')
                    else:
                        print("#", end='')
                print()
