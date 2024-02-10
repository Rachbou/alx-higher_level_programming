#!/usr/bin/python3
# 5-text_indentation.py
# Rachid BOULMANI
"""a function that prints a text with 2 new lines after
each of these characters: '.', '?' and ':'
args :
    text : must be a string.
"""


def text_indentation(text):
    """a function that prints a text with 2 new lines after
    each of these characters: '.', '?' and ':'
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    for idx in range(len(text)):
        if text[idx] in characters:
            print(text[idx])
            print()
        elif text[idx] == ' ' and text[idx - 1] in characters:
            pass
        else:
            print(text[idx], end='')
