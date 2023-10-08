#!/usr/bin/python3
"""Use list comprehension to create a new string without 'c' and 'C'"""


def no_c(my_string):
    new_string = ''.join(char for char in my_string if char.lower() not in {'c', 'C'})
    return new_string
