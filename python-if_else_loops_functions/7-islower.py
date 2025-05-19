#!/usr/bin/python3
def islower(c):
    '''Check if a character is a lowercase letter

    Args:
        c (char): character to check

    Returns:
        bool: True if lowercase, False otherwise
    '''
    return ord('a') <= ord(c) <= ord('z')
