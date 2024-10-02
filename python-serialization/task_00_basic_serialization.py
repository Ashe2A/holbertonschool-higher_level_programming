#!/usr/bin/python3
"""
Basic serialization.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialization.
    """
    with open(filename, 'w') as file:
        json.dumps(data, file)


def load_and_deserialize(filename):
    """
    Deserialization.
    """
    with open(filename, 'r') as file:
        return json.loads(file)
