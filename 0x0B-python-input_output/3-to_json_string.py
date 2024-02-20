#!/usr/bin/python3
# 3-to_json_string.py
# Rachid BOULMANI
"""
a function that returns the JSON representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)
    """

    s_my_obj = json.dumps(my_obj)
    return (s_my_obj)
