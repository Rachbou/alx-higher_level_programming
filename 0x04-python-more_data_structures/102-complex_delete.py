#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        values = list(a_dictionary.values())
        keys = list(a_dictionary.keys())
        key = keys[values.index(value)]
        del a_dictionary[key]
    return (a_dictionary)
