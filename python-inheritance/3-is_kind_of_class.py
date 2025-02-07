#!/usr/bin/python3
"""
Is kind of class.
"""


def is_same_class(obj, a_class):
    """Checks if obj is of or inherits the same class as a_class

    Args:
        obj (a_class): The object
        a_class (any class): The class

    Returns:
        boolean: True if same class or inherited, false otherwise
    """
    return issubclass(type(obj), a_class)
