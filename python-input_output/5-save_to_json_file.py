#!/usr/bin/python3
'''Save Object to a file'''
import json


def save_to_json_file(my_obj, filename):
    '''Writes an object's JSON string representation into an file

    Args:
        my_str (obj): The JSON string
        filename (str): The files name
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(json.dumps(my_obj))
