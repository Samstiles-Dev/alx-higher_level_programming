#!/usr/bin/python3
"""function that does exactly the same as the following Python bytecode"""


def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return (a * b) - c
