#!/usr/bin/python3
def max_integer(my_list=[]):
    maximum = 0
    for integer in my_list:
        if integer > maximum:
            maximum = integer
    return (maximum)
