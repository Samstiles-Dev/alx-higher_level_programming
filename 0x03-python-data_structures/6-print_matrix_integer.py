#!/usr/bin/python3
"""function that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col, element in enumerate(row):
            if col == len(row) - 1:
                print("{:d}".format(element), end="")
            else:
                print("{:d} ".format(element), end="")
        print()
