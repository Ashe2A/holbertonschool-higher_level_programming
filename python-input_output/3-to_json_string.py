#!/usr/bin/python3
'''To JSON string'''
import json


def to_json_string(my_obj):
    '''Convert an object's JSON into a string representation

    Args:
        my_obj (obj): The object.
    '''
    return json.dumps(my_obj)
