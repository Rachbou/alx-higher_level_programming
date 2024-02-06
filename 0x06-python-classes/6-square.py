#!/usr/bin/python3
class Square:
    """
    class Square that defines a square by:
    (based on 2-square.py)
    Private instance attribute: size
    property def size(self): to retrieve it
    property setter def size(self, value): to set it
    with size must be an integer >= 0
    Private instance attribute: position:
    property def position(self): to retrieve it
    property setter def position(self, value): to set it:
    position must be a tuple of 2 positive integers, otherwise
    raise a TypeError exception with the message
    position must be a tuple of 2 positive integers
    Instantiation with optional size and optional position
    Public instance method: def area(self):
    that returns the current square area
    and Public instance method: def my_print(self):
    that prints in stdout the square with the character #
    if size is equal to 0, print an empty line
    position should be use by using space
    Don’t fill lines by spaces when position[1] > 0
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return(self.__size)

    @property
    def position(self):
        return(self.__position)

    @size.setter
    def size(self, size):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, position):
        if isinstance(position[0], int) and isinstance(position[1], int):
            if position[0] < 0 or position[1] < 0:
                raise TypeError("position must be a tuple \
                                of 2 positive integers")
            self.__position = position
        else:
            raise TypeError("position must be a tuple \
                            of 2 positive integers")

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
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
