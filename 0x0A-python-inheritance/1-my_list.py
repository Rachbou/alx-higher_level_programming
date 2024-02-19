#!/usr/bin/python3
# FileName.py
# Rachid BOULMANI
"""
a class MyList that inherits from list
"""


class MyList(list):
    """
    a class MyList that inherits from list
    with Public instance method print_sorted():
        prints the list, but sorted (ascending sort)
    """

    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order
        """

        print(sorted(self))
