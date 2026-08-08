#!/usr/bin/python3
"""Module for dividing all elements of a matrix by a number.
This module provides a function that returns a new matrix
with all elements divided by a given divisor, rounded to
2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    Args:
        matrix: A list of lists of integers or floats.
        div: The divisor, an integer or float.
    Returns:
        list: A new matrix with each element divided by div,
            rounded to 2 decimal places.
    Raises:
        TypeError: If matrix is not a list of lists of int/float,
            if rows aren't the same size, or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not all(isinstance(n, (int, float)) and
                   not isinstance(n, bool) for n in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(n / div, 2) for n in row] for row in matrix]
    return new_matrix
