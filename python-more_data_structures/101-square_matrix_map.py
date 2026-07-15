#!/usr/bin/python3
"""Module that squares all integers of a matrix, using map."""
def square_matrix_map(matrix=[]):
    """Return a new matrix with each value squared, using map."""
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
