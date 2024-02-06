#!/usr/bin/python3
class Square:
    """
    class Square that defines a square by:
    (based on 2-square.py)
    Private instance attribute: size
    property def size(self): to retrieve it
    property setter def size(self, value): to set it
    with size must be an integer >= 0
    Instantiation with optional size
    Public instance method: def area(self):
    that returns the current square area
    and Public instance method: def my_print(self):
    that prints in stdout the square with the character #
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
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
        return (self.__size ** 2)

    def my_print(self):
        for i in range(self.size):
            for j in range(self.size):
                print("#", end='')
            print()
        if self.size == 0:
            print()
