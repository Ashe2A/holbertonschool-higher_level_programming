#!/usr/bin/python3

"""
Append file.
"""


def append_write(filename="", text=""):
    """
    Appending the file.
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
