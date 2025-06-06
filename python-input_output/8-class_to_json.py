#!/usr/bin/python3
'''Class to JSON'''
import json


def class_to_json(obj):
    '''Creates an object with its JSON string representation read in a file

    Args:
        obj (obj): The file name containing the JSON dump
    '''
    return obj.__dict__
