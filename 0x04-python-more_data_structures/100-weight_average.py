#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) < 1:
        return (0)
    total_weight = sum(map(lambda x: x[1], my_list))
    total_score = sum(map(lambda x: x[0] * x[1], my_list))
    average = total_score / total_weight
    return (average)
