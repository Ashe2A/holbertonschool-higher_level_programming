#!/usr/bin/python3
def no_c(my_string):
    """Removes Cs from a string

    Args:
        my_string (str): The string

    Returns:
        The string without Cs
    """
    new_string = ""
    for i in my_string:
        if i != "c" and i != "C":
            new_string += i
    return new_string
