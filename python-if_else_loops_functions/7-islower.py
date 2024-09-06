#!/usr/bin/python3
def islower(c):
    """
    Check if a character is a lowercase letter.

    Parameters:
        c (str): Character to check.

    Returns:
        bool: True if lowercase, False otherwise.
    """
    return ord('a') <= ord(c) <= ord('z')
