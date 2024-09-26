#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Add two integers.
    """
    a = int(a)
    b = int(b)
    if not (isinstance(a, int)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int)):
        raise TypeError("b must be an integer")
    return a + b
