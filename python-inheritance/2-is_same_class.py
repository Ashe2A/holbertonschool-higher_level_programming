#!/usr/bin/python3

"""
Is same class.
"""


def is_same_class(obj, a_class):
    """
    Checks if the object is of a class.

    Paremeters:
        obj: The object
        a_class: a class$

    Return:
        True is obj is from a class, False otherwise
    """

    return type(obj) is a_class
