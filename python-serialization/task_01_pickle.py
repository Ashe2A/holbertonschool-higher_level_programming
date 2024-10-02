#!/usr/bin/python3
"""
Basic serialization with pickle.
"""

import pickle
import os


def serialize_and_save_to_file(data, filename):
    """
    Serialization with pickle.
    """
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, 'w') as file:
        pickle.dumps(data, file)


def load_and_deserialize(filename):
    """
    Deserialization with pickle.
    """
    with open(filename, 'r') as file:
        return pickle.loads(file)
