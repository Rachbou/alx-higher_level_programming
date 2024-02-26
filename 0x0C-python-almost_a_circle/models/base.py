#!/usr/bin/python3
# base.py
# Rachid BOULMANI
"""
the 'base' of all other classes in this project.
The goal of it is to manage id attribute in all the future classes
and to avoid duplicating the same code
"""

import json
import csv
import turtle


class Base:
    """
    Class Base with:
        private class attribute __nb_objects (integer)
        public instance attribute id - (integer)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor:
        if id is not None:
            assign the public instance attribute id with this argument value
        otherwise:
            increment __nb_objects and assign the new value to the public
            instance attribute id
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries:
            list_dictionaries is a list of dictionaries
            If list_dictionaries is None or empty:
                Returns the string: "[]"
            Otherwise:
                Returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as file:
            if list_objs is None:
                list_dict = []
            else:
                list_dict = [obj.to_dictionary()
                             for obj in list_objs]
            file.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
            json_string is a string representing a list of dictionaries
            If json_string is None or empty:
                Returns an empty list
            Otherwise:
                Returns the list represented by json_string
        """
        if json_string is None or json_string == '':
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set:
            **dictionary can be thought of as a double pointer to a dictionary
        """
        if dictionary and len(dictionary) != 0:
            if cls.__name__ == "Square":
                NewCls = cls(1)
            else:
                NewCls = cls(1, 1)
            NewCls.update(**dictionary)
            return (NewCls)

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances:
            The filename must be: <Class name>.json - example: Rectangle.json
            If the file doesn’t exist:
                Return an empty list
            Otherwise:
                Return a list of instances - the type of these instances
                depends on cls (current class using this method)
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as file:
                list_dicts = Base.from_json_string(file.read())
                return ([cls.create(**dictionary)
                         for dictionary in list_dicts])
        except IOError:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes the writes list_objs to a CSV file.
        Format of the CSV:
            Rectangle: <id>,<width>,<height>,<x>,<y>
            Square: <id>,<size>,<x>,<y>
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w", newline="") as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == "Square":
                    names = ['id', 'size', 'x', 'y']
                else:
                    names = ['id', 'width', 'height', 'x', 'y']
                writer = csv.DictWriter(file, fieldnames=names)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Returns a list of instances:
            The filename must be: <Class name>.csv - example: Rectangle.csv
            Format of the CSV:
                Rectangle: <id>,<width>,<height>,<x>,<y>
                Square: <id>,<size>,<x>,<y>
            If the file doesn’t exist:
                Return an empty list
            Otherwise:
                Return a list of instances - the type of these instances
                depends on cls (current class using this method)
        """
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, "r", newline="") as file:
                if cls.__name__ == "Square":
                    names = ["id", "size", "x", "y"]
                else:
                    names = ["id", "width", "height", "x", "y"]
                list_dicts = csv.DictReader(file, fieldnames=names)
                list_dictionaries = [dict([k, int(v)]
                                          for k, v in dictionary.items())
                                     for dictionary in list_dicts]
                return ([cls.create(**dictionary)
                         for dictionary in list_dictionaries])
        except IOError:
            return ([])

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
