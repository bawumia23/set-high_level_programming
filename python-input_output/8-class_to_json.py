#!/usr/bin/python3
"""Module to convert class instance to JSON serializable dict."""


def class_to_json(obj):
    """Return the dictionary description with simple data structure.

    The dictionary is for JSON serialization of an object.
    """
    Args:
        obj: An instance of a Class.

    Returns:
        A dictionary representation of the object.
    """
    return obj.__dict__
