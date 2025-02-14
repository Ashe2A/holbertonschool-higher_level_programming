#!/usr/bin/python3

"""
Write file.
"""


def write_file(filename="", text=""):
    """
    Writing the file.

    Parameters:
        filename (string): the file name
        text (string): the input

    Returns:
        New file with the file's content
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
