#!/usr/bin/python3

"""
Append file.
"""


def append_write(filename="", text=""):
    """
    Appending the file.

    Parameters:
        filename (string): the file name
        text (string): the input

    Returns:
        New file with the file's content
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
