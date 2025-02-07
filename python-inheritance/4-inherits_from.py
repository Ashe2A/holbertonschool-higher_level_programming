#!/usr/bin/python3
"""
Inherits from.
"""


def inherits_from(obj, a_class):
    """Checks if obj inherits the same class as a_class

    Args:
        obj (a_class): The object
        a_class (any class): The class

    Returns:
        boolean: True if inherited class, false otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
