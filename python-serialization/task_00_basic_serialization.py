#!/usr/bin/python3

import pickle

def serialize_and_save_to_file(data, filename):
    with open(filename, 'w') as file:
        pickle.dump(data, file)

def load_and_deserialize(filename):
    with open(filename, 'r') as file:
        pickle.load(file)
    return file.__dict__
