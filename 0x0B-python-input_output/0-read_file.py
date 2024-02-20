#!/usr/bin/python3
# 0-read_file.py
# Rachid BOULMANI
"""
a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    a function that reads a text file (UTF8)
    and prints it to stdout
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
