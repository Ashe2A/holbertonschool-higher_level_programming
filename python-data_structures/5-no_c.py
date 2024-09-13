#!/usr/bin/python3

def no_c(my_string):
    """
    Removes c's from a string.

    Parameters:
        my_string (string) : the string.

    Returns:
        The modified (or not) string.
    """
    new_string = ""
    for i in my_string:
        if (i != 'C') and (i != 'c'):
            new_string += i
    my_string = new_string
    return my_string
