#!/usr/bin/python3
# 4-print_square.py
# Rachid BOULMANI
"""function that prints a square with the character #.
args :
    size : must be an integer
"""


def print_square(size):
    """
    function that prints a square with the character #.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print('#', end='')
            print()
