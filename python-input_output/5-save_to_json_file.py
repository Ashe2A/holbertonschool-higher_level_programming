#!/usr/bin/python3

"""
Writes object to text file.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writing object to text file.

    Parameters:
        my_obj: object.
        filename (string): the file to save in.
    """

    with open(filename, 'w', encoding="utf-8") as filename:
        filename.write(json.dumps(my_obj))
