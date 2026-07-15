#!/usr/bin/python3
"""Module that returns a new dictionary with all values multiplied by 2."""


def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary (dict): the dictionary, all values are integers.

    Returns:
        dict: a new dictionary with all values multiplied by 2.
    """
    return {key: value * 2 for key, value in a_dictionary.items()}
