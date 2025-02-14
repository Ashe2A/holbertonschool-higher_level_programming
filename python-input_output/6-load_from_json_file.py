#!/usr/bin/python3

"""
Loads object from JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Loading object from JSON file.

    Parameters:
        my_obj: object.
        filename (string): the file to convert.

    Return:
        The object from the JSON file
    """

    with open(filename, 'r', encoding="utf-8") as file:
        return json.loads(file.read())
