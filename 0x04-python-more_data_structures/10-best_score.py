#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        values = list(a_dictionary.values())
        keys = list(a_dictionary.keys())
        if len(values) > 0:
            best_score = max(values)
            best_key = keys[values.index(best_score)]
            return (best_key)
