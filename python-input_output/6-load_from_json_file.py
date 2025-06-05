#!/usr/bin/python3
'''Create object from a JSON file'''
import json


def load_from_json_file(filename):
    '''Creates an object with its JSON string representation read in a file

    Args:
        filename (str): The file name containing the JSON dump
    '''
    with open(filename, encoding='utf-8') as f:
        return json.loads(f.read())
