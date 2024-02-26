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
        return (self.__x)

    @property
    def y(self):
        """y's getter"""
        return (self.__y)

    @width.setter
    def width(self, width):
        """width's setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """height's setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """x's setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """y's setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area value of the Rectangle instance."""
        area = self.width * self.height
        return (area)

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x, end='')
            for j in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        """string representation of a Rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute:
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        """
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.__init__(self.width, self.height,
                                  self.x, self.y, args[i])
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
                else:
                    break
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.__init__(self.width, self.height,
                                  self.x, self.y, value)
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                else:
                    pass
        else:
            pass

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle:
        {"id": self.id,
        "width": self.width
        "height": self.height
        "x": self.x
        "y": self.y}
        """
        dictionary = {
                    "id": self.id,
                    "width": self.width,
                    "height": self.height,
                    "x": self.x,
                    "y": self.y
                    }
        return (dictionary)
