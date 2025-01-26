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
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    c = int(a)
    d = int(b)
    print("{:d}".format(c + d))
