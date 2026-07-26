#!/usr/bin/python3
"""Module that defines a LockedClass."""


class LockedClass:
    """Prevent dynamic creation of new instance attributes.

    The only new instance attribute allowed to be created is
    ``first_name``. Any other attribute must already exist.
    """

    def __setattr__(self, name, value):
        """Restrict attribute creation to 'first_name' only."""
        if name != "first_name" and not hasattr(self, name):
            raise AttributeError(
                "'{}' object has no attribute '{}'".format(
                    type(self).__name__, name))
        super().__setattr__(name, value)
