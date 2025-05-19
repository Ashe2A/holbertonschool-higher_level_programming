#!/usr/bin/python3
"""Say my name"""


def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    else:
        if not isinstance(last_name, str):
            last_name = ""
            raise TypeError("last_name must be a string")
        print("My name is {} {}".format(first_name, last_name))
