#!/usr/bin/python3
"""Module for dividing a matrix by a number.

This module provides a function that divides all elements
of a matrix by a given divisor, rounding to 2 decimals.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a number.

    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float) to divide by.

    Returns:
        list: A new matrix with all elements divided by div,
              rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats,
                   if rows are not the same size, or if div is not
                   a number.
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        if len(row) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of "
                    "integers/floats"
                )

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
