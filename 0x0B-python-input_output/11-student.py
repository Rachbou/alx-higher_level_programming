#!/usr/bin/python3
# 11-student.py
# Rachid BOULMANI
"""
a class Student that defines a student  (based on 10-student.py)
"""


class Student:
    """
    a class Student that defines a student by:
        Public instance attributes:
            first_name
            last_name
            age
        Public method def to_json(self, attrs=None):
            Retrieves a dictionary representation of a Student instance
        Public method def reload_from_json(self, json):
            Replaces all attributes of the Student instance
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation with:
            first_name, last_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance:
            If attrs is a list of strings, only attribute names contained in
            this list must be retrieved.
            Otherwise, all attributes must be retrieved
        """
        attributs = self.__dict__
        if type(attrs) is list and all(type(att) is str for att in attrs):
            attributs = {k: getattr(self, k)
                         for k in attrs
                         if hasattr(self, k)}
        return (attributs)

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance:
            json will always be a dictionary
            A dictionary key will be the public attribute name
            A dictionary value will be the value of the public attribute
        """
        for name, value in json.items():
            setattr(self, name, value)
