#!/usr/bin/python3
"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """Checks if object is from the same class or a subclass

    Args:
        obj (obj): The object to identify
        a_class (class): The class to check

    Returns:
        bool: True if obj is a_class or subclass of, False otherwise
    """
    return isinstance(obj, a_class)
