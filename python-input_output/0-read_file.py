#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """Read file with a filename

    Args:
        filename (str, optional): Name of the file. Defaults to empty string.
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    print(read_data, end="")
