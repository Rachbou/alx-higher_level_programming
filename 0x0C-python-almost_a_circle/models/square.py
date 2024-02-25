#!/usr/bin/python3
# square.py
# Rachid BOULMANI
"""
the class 'Square' that inherits from the class 'Rectangle'.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square with:
        inheriting from the class 'Rectangle'
        overriding the __str__ method
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        class constructor:
            Call the super class with id, x, y, width and height
            width = height = size
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of a Square"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.size))

    @property
    def size(self):
        """size's getter"""
        return (self.width)

    @size.setter
    def size(self, size):
        """size's setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute:
            *args is the list of arguments - no-keyworded arguments:
                1st argument should be the id attribute
                2nd argument should be the size attribute
                3rd argument should be the x attribute
                4th argument should be the y attribute
            **kwargs can be thought of as a double pointer to a dictionary
            **kwargs must be skipped if *args exists and is not empty
            Each key in this dictionary represents an attribute to the instance
        """
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.__init__(self.size, self.x,
                                  self.y, args[i])
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
                else:
                    break
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.__init__(self.size, self.x,
                                  self.y, value)
                elif key == "size":
                    self.width = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                else:
                    pass
        else:
            pass
