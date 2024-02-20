#!/usr/bin/python3
# 5-save_to_json_file.py
# Rachid BOULMANI
"""
a function that writes an Object to a text file,
using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file,
    using a JSON representation
    """

    with open(filename, 'w') as file:
        s_my_obj = json.dumps(my_obj)
        file.write(s_my_obj)
