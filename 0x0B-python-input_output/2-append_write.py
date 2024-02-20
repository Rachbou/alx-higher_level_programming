#!/usr/bin/python3
# 2-append_write.py
# Rachid BOULMANI
"""
a function that appends a string at the end of a text file (UTF8)
"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as file:
        Nbre = file.write(text)
    return (Nbre)
