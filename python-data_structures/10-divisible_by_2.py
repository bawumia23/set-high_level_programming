#!/usr/bin/python3
"""Module that finds all multiples of 2 in a list."""


def divisible_by_2(my_list=[]):
    """Return a new list of booleans indicating which elements
    of my_list are divisible by 2.
    """
    result = []
    for num in my_list:
        result.append(num % 2 == 0)
    return result
