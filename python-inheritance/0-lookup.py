#!/usr/bin/python3
"""
Lookup.
"""


def lookup(obj):
    """Lookup properties of specified object

    Args:
        obj (object type): class instance

    Returns:
        list: list of attributes and methods of obj
    """
    return dir(obj)
