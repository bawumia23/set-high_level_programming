#!/usr/bin/python3
"""Module that defines a LockedClass."""


class LockedClass:
    """Prevent dynamic creation of new instance attributes.

    The only instance attribute allowed to be set is ``first_name``.
    """

    __slots__ = ('first_name',)
