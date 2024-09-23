#!/usr/bin/python3
def lookup(obj):
    """
    Available attributes and methods of an object.

    Parameters:
        obj: The objet.

    Returns:
        list of attributes and methods of obj
    """
    return dir(obj)
