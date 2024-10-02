#!/usr/bin/python3

"""
Basic serialization.
"""

import pickle


def serialize_and_save_to_file(data, filename)
    """
    Serialization.
    """

    with open(filename, 'wb') as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    """
    Deserialization.
    """

    with open(filename, 'rb') as file:
        loaded_file = pickle.load(file)
    return loaded_file
