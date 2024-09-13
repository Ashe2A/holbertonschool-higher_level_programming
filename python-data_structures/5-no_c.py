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
        if (my_string[i - 1] == "C") or (my_string[i - 1] == "c"):
            del(my_string[i - 1])
    return my_string
