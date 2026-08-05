#!/usr/bin/python3
"""Module for Student class."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of a Student.

        If attrs is provided, only include those attributes.
        """
        if attrs is None:
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance.

        Use the key-value pairs from the json dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
