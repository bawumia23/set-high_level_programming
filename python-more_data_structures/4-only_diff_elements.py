#!/usr/bin/python3
"""Module that returns a set of elements present in only one set."""


def only_diff_elements(set_1, set_2):
    """Return a set of all elements present in only one set.

    Args:
        set_1 (set): the first set.
        set_2 (set): the second set.

    Returns:
        set: elements present in only one of set_1 or set_2.
    """
    return set_1 ^ set_2
