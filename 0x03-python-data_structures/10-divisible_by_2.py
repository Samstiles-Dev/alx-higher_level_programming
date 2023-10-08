#!/usr/bin/python3
"""a function that finds all multiples of 2 in a list."""


def divisible_by_2(my_list=[]):
    result = [num % 2 == 0 for num in my_list]
    return result
