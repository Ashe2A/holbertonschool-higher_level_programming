#!/usr/bin/python3
"""Class to JSON"""
import json


def class_to_json(obj):
    """Gets an object's dictionary convertible into JSON format

    Args:
        obj (obj): The object
    """
    return obj.__dict__
