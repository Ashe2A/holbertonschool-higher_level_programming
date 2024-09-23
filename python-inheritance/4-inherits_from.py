#!/usr/bin/python3

"""
Inherits from.
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is of a subclass of a class only.

    Parameters:
        obj: The object
        a_class: a class

    Return:
        True is obj is from a subclass of the class,
        False if of class and otherwise
    """

    return issubclass(type(obj), a_class) and not (type(obj) is a_class)
