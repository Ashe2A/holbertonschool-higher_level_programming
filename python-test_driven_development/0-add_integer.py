#!/usr/bin/python3
"""
Add integer.
add_integer is the function to add integers
Usage: x = add_integer(a, b)
"""


def add_integer(a, b=98):
    """
    Add two integers together.

    Params:
        a: first integer
        b: second

    Return:
        Sum of a and b
    """
    a_int = "a must be an integer"
    b_int = "b must be an integer"
    if not isinstance(a, (int, float)):
        raise TypeError(a_int)

    if not isinstance(b, (int, float)):
        raise TypeError(b_int)

    c = int(a)
    d = int(b)
    return c + d
