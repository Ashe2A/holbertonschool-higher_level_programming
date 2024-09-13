#!/usr/bin/python3

def no_c(my_string):
    """
    Removes c's from a string.

    Parameters:
        my_string (string) : the string.

    Returns:
        The modified (or not) string.
    """
    for i in my_string:
        if (i == 'C') or (i == 'c'):
            replace(i, '')
    return my_string
