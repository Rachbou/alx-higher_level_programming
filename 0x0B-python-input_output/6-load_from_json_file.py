#!/usr/bin/python3
# 6-load_from_json_file.py
# Rachid BOULMANI
"""
a function that creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """
    a function that creates an Object from a “JSON file”
    """

    with open(filename, 'r') as file:
        my_str = file.read()
        my_obj = json.loads(my_str)
    return (my_obj)
