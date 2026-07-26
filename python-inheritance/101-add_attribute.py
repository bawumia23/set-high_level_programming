#!/usr/bin/python3
"""Module that adds an attribute to an object if possible."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object, if the object allows it.

    Args:
        obj: the object to modify.
        name (str): the name of the attribute to add.
        value: the value to assign to the attribute.

    Raises:
        TypeError: if the object does not support dynamic attribute
            creation.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
