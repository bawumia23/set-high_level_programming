#!/usr/bin/python3
"""Module that checks class inheritance relationships for an object."""


def inherits_from(obj, a_class):
    """Check if an object belongs to a strict subclass of the
    specified class.

    Args:
        obj: the object to check.
        a_class: the base class to compare against.

    Returns:
        bool: True if obj's type is a subclass of a_class but not
            a_class itself, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
