#!/usr/bin/python3

"""
Read file.
"""


def read_file(filename=""):
    """
    Reading the file.

    Parameters:
        filename (string): the file name
    """
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
