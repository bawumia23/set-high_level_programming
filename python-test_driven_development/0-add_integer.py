#!/usr/bin/python3
"""Module for adding two integers.

This module provides a function that adds two integers
or floats, casting floats to integers before addition.
"""


def add_integer(a, b=98):
    """Add two integers.

    Args:
        a: First number, must be int or float.
        b: Second number, must be int or float (default is 98).

    Returns:
        int: The addition of a and b as integers.

    Raises:
        TypeError: If a or b is not an int or float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
