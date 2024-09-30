#!/usr/bin/python3

"""
Read file.
"""


def read_file(filename=""):
    """
    Reading the file.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
