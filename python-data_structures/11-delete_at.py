#!/usr/bin/python3
"""Module that deletes an item at a specific position in a list."""


def delete_at(my_list=[], idx=0):
    """Delete the item at idx in my_list, in place.

    If idx is negative or out of range, my_list is unchanged.
    Returns my_list.
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    my_list[idx:idx + 1] = []
    return my_list
