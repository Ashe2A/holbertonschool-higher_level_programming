#!/usr/bin/python3

""" Tests function to add integers with exceptions """


def add_integer(a, b=98):
    """ Add two integers """
    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
