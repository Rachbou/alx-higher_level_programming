#!/usr/bin/python3
# 4-from_json_string.py
# Rachid BOULMANI
"""
a function that returns an object (Python data structure)
represented by a JSON string
"""

import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure)
    represented by a JSON string
    """

    my_obj = json.loads(my_str)
    return (my_obj)
