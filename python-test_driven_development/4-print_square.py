#!/usr/bin/python3
"""Print square"""


def print_square(size):
    """Prints a square of variable size

    Args:
        size (int): the size

    Raises:
        TypeError: If not int (floats don't work)
        ValueError: If size is negative
    """
    if not isinstance(size, int) or isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
