#!/usr/bin/python3
"""
Pickle serialization.
"""

import pickle

def serialize_and_save_to_file(data, filename):
    """
    Pickle Serialization.
    """
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    """
    Pickle Deserialization.
    """
    with open(filename, 'rb') as file:
        return pickle.load(file)
