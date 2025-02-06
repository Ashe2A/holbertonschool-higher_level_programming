#!/usr/bin/python3
"""
Is same class.
"""


def is_same_class(obj, a_class):
    """Checks if obj is of the same class as a_class

    Args:
        obj (a_class): The object
        a_class (any class): The class

    Returns:
        boolean: True if same class, false otherwise
    """
    return type(obj) is a_class
