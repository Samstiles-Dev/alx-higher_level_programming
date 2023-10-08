#!/usr/bin/python3
"""a function that finds all multiples of 2 in a list."""


def divisible_by_2(my_list=[]):
    array_list = my_list[:]
    for ind, val in enumerate(my_list):
        if val % 2 == 0:
            array_list[ind] = True
        else:
            array_list[ind] = False
    return(array_list)
