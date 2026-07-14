#!/usr/bin/python3
"""Module that adds two tuples."""


def add_tuple(tuple_a=(), tuple_b=()):
    """Return a tuple that is the element-wise sum of the first
    two elements of tuple_a and tuple_b, padding missing values
    with 0.
    """
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (a1 + b1, a2 + b2)
