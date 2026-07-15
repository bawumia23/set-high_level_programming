#!/usr/bin/python3
"""Module that computes the square value of all integers of a matrix."""


def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix.

    Args:
        matrix (list): a 2 dimensional array of integers.

    Returns:
        list: a new matrix with each value squared.
    """
    return [[value ** 2 for value in row] for row in matrix]
