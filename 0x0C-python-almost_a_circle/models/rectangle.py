#!/usr/bin/python3
# rectangle.py
# Rachid BOULMANI
"""
the class 'Rectangle' that inherits from the class 'Base'.
"""

from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle with:
        private class attributes, each with its own getter and setter:
            __width -> width (integer)
            __height -> height (integer)
            __x -> x (integer)
            __y -> y (integer)
        public instance attribute id - (integer)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor:
            Call the super class with id
            Assign each argument:
                width,
                height,
                x and y
            to the right attribute
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width's getter"""
        return (self.__width)

    @property
    def height(self):
        """height's getter"""
        return (self.__height)

    @property
    def x(self):
        """x's getter"""
        return(self.__x)

    @property
    def y(self):
        """y's getter"""
        return(self.__y)

    @width.setter
    def width(self, width):
        """width's setter"""
        self.__width = width

    @height.setter
    def height(self, height):
        """height's setter"""
        self.__height = height

    @x.setter
    def x(self, x):
        """x's setter"""
        self.__x = x

    @y.setter
    def y(self, y):
        """y's setter"""
        self.__y = y
