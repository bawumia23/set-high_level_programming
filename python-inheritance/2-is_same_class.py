#!/usr/bin/python3
"""Module that checks if an object is exactly an instance of a class."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of the specified class.

    Args:
        obj: the object to check.
        a_class: the class to compare against.

    Returns:
        bool: True if type(obj) is exactly a_class, otherwise False.
    """
    return type(obj) is a_class
