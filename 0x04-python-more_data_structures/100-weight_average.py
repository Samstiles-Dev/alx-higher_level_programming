#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    value = 0
    value2 = 0
    for a, b in my_list:
        value += a * b
        value2 += b
    return (value / value2)
