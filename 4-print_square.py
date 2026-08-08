#!/usr/bin/python3
"""Module for printing a square.

This module provides a function that prints a square
of a given size using the '#' character.
"""


def print_square(size):
    """Print a square with the character '#'.

    Args:
        size: The size length of the square, must be an integer.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
