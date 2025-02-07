#!/usr/bin/python3
"""
Is kind of class.
"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is of or inherits the same class as a_class

    Args:
        obj (a_class): The object
        a_class (any class): The class

    Returns:
        boolean: True if same class or inherited, false otherwise
    """
    return issubclass(obj, a_class) or type(obj) is a_class
