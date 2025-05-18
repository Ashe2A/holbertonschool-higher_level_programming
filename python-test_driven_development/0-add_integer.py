#!/usr/bin/python3
"""Integers addition"""

def add_integer(a, b=98):
    """Adds integers

    Args:
        a (int): first integer
        b (int, optional): second integer. Defaults to 98.

    Raises:
        TypeError: if a isn't int or float
        TypeError: if b isn't int or float

    Returns:
        int: sum of the two integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
