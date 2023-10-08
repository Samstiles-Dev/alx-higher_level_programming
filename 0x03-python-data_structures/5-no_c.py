#!/usr/bin/python3
"""Use list comprehension to create a new string without c and C"""


def no_c(my_string):
    new_string = ("".join(c for c in my_string if c not in "Cc"))
    return new_string
