#!/usr/bin/python3
"""Module that checks if an object is an instance of a class or subclass."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class or one of its
    subclasses.

    Args:
        obj: the object to check.
        a_class: the class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or one of its
            subclasses, otherwise False.
    """
    return isinstance(obj, a_class)
