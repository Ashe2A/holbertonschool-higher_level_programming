#!/usr/bin/python3

"""
Is kind of class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is of a subclass of a class.

    Parameters:
        obj: The object
        a_class: a class

    Return:
        True is obj is from a subclass of the class, False otherwise
    """

    return issubclass(type(obj), a_class)
