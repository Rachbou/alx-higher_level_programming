#!/usr/bin/python3
# 9-rectangle.py
# Rachid BOULMANI
"""Define a class Rectangle."""


class Rectangle:
    """
    a class Rectangle that defines a rectangle by:
    (based on 8-rectangle.py)
    Private instance attribute: width, must be an integer >= 0
    Private instance attribute: height, must be an integer >= 0
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """property def width(self): to retrieve width"""
        return (self.__width)

    @property
    def height(self):
        """property def height(self): to retrieve height"""
        return (self.__height)

    @width.setter
    def width(self, value):
        """property setter def width(self, value): to set width
        with width must be an integer >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """property setter def height(self, value): to set height
        with height must be an integer >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method that
        returns the rectangle area
        """
        result = self.width * self.height
        return (result)

    def perimeter(self):
        """Public instance method that
        returns the rectangle perimeter
        """
        if self.area == 0:
            return (0)
        result = 2 * (self.width + self.height)
        return (result)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method that returns the biggest rectangle
        based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return (rect_2)
        else:
            return (rect_1)

    @classmethod
    def square(cls, size=0):
        """Class method def square(cls, size=0): that returns
        a new Rectangle instance with width == height == size
        """
        return (cls(size, size))

    def __str__(self):
        """Define the print() representation of a Rectangle."""

        RectangleStr = []
        if self.area == 0:
            return ('')
        for i in range(1, self.height + 1):
            for j in range(self.width):
                RectangleStr.append(str(self.print_symbol))
            if i < self.height:
                RectangleStr.append('\n')
        return (''.join(RectangleStr))

    def __repr__(self):
        """Define the string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return('Rectangle({:d}, {:d})'.format(self.width, self.height))

    def __del__(self):
        """Prints the message Bye rectangle...
        when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
