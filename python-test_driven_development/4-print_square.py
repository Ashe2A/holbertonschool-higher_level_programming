#!/usr/bin/python3
"""
Print square.
Usage: print_square(size)
"""


def print_square(size):
    """
    Print a square with variable size.

    Params:
        size: The size of the square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
