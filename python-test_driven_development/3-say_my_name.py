#!/usr/bin/python3
"""Say my name"""


def say_my_name(first_name, last_name=""):
    """Prints a full name

    Args:
        first_name (str): The first name
        last_name (str, optional): The last name. Defaults to empty string.

    Raises:
        TypeError: If the first name isn't a string
        TypeError: If the last name isn't a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    else:
        if not isinstance(last_name, str):
            last_name = ""
            raise TypeError("last_name must be a string")
        print("My name is {} {}".format(first_name, last_name))
