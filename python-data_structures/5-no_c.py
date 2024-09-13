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
        if (ord(my_string[i - 1]) == ord('C'))\
        or (ord(my_string[i - 1]) == ord('c')):
            del(my_string[i - 1])
    return my_string
