#!/usr/bin/python3
"""Module defining the Student class with serialization and deserialization."""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance.

        Args:
            first_name: The student's first name.
            last_name: The student's last name.
            age: The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        Args:
            attrs: A list of attribute names to retrieve. If None, all attributes are retrieved.

        Returns:
            A dictionary representation of the Student.
        """
        if attrs is None:
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json: A dictionary with attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
