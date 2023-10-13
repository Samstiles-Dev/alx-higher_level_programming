#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for k in matrix:
        squared_matrix.append([c**2 for c in k])
    return squared_matrix
