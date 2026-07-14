#!/usr/bin/python3
"""Module that replaces an element in a copy of a list."""


def new_in_list(my_list, idx, element):
    """Return a copy of my_list with element at idx replaced.

    If idx is negative or out of range, return a copy of the
    original list unchanged.
    """
    new_list = my_list[:]
    if idx < 0 or idx > len(my_list) - 1:
        return new_list
    new_list[idx] = element
    return new_list
