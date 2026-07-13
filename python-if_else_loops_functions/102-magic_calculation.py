#!/usr/bin/python3
"""Module for magic_calculation, derived from Python bytecode."""


def magic_calculation(a, b, c):
    """Perform a calculation based on comparisons of a, b, and c.

    Args:
        a: first value
        b: second value
        c: third value

    Returns:
        c if a < b
        a + b if c > b
        a * b - c otherwise
    """
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c
