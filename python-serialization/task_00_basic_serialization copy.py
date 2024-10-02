#!/usr/bin/python3
"""
Basic serialization.
"""

import pickle
import os


def serialize_and_save_to_file(data, filename):
    """
    Serialization.
    """
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, 'w') as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    """
    Deserialization.
    """
    with open(filename, 'r') as file:
        loaded_file = pickle.load(file)
    return loaded_file
