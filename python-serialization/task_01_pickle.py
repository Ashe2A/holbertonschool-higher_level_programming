#!/usr/bin/python3
"""
Basic serialization with pickle.
"""

import pickle


def serialize_and_save_to_file(data, filename):
    """
    Serialization with pickle.
    """
    with open(filename, 'w') as file:
        pickle.dumps(data, file)


def load_and_deserialize(filename):
    """
    Deserialization with pickle.
    """
    with open(filename, 'r') as file:
        return pickle.loads(file)
