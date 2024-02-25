#!/usr/bin/python3
# base.py
# Rachid BOULMANI
"""
the 'base' of all other classes in this project.
The goal of it is to manage id attribute in all the future classes
and to avoid duplicating the same code
"""

import json


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
