#!/usr/bin/python3
"""Module that prints a dictionary by ordered keys."""


def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys.

    Args:
        a_dictionary (dict): the dictionary to print, all keys are strings.
    """
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
