#!/usr/bin/python3
"""
Basic serialization.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialization.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(json.dumps(data))


def load_and_deserialize(filename):
    """
    Deserialization.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.loads(file.read())
