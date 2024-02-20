#!/usr/bin/python3
# 8-class_to_json.py
# Rachid BOULMANI
"""
a function that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    a function that returns the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """

    s_obj = obj.__dict__
    return (s_obj)
