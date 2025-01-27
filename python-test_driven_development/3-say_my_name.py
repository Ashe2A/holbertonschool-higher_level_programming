#!/usr/bin/python3
"""
Say my name.
Usage: say_my_name(first_name, last_name)
"""


def say_my_name(first_name, last_name=""):
    """
    Print a full name.

    Params:
        first_name: The first name
        last_name: The last name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
