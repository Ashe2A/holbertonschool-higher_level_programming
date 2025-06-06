#!/usr/bin/python3
"""Lookup"""


def lookup(obj):
    """Lookup attributes of an object

    Args:
        obj (obj): An object

    Returns:
        list: List of the object's attributes
    """
    return list(dir(obj))
