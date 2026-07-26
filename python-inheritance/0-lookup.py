#!/usr/bin/python3
"""Module that returns the available attributes and methods of an object."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: the object to inspect.

    Returns:
        list: the sorted list of attribute and method names.
    """
    return dir(obj)
