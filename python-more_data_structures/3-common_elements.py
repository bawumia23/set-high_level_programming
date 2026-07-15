#!/usr/bin/python3
"""Module that returns a set of common elements in two sets."""


def common_elements(set_1, set_2):
    """Return a set of common elements in two sets.

    Args:
        set_1 (set): the first set.
        set_2 (set): the second set.

    Returns:
        set: elements present in both set_1 and set_2.
    """
    return set_1 & set_2
