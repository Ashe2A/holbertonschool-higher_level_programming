#!/usr/bin/python3
"""Basic Serialization"""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a Python dictionary to a JSON file

    Args:
        data (dict): A Python Dictionary with data
        filename (str): The filename of the output JSON file.
            If the output file already exists it should be replaced.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(data))


def load_and_deserialize(filename):
    """Deserialize a JSON file into a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: Python Dictionary with the deserialized JSON data from the file.
    """
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
