#!/usr/bin/python3
# 1-write_file.py
# Rachid BOULMANI
"""
a function that writes a string to a text file (UTF8)
"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as file:
        Nbre = file.write(text)
    return (Nbre)
