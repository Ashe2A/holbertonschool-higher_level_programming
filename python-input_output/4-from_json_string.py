#!/usr/bin/python3
"""From JSON string to Object"""
import json


def from_json_string(my_str):
    """Convert an object's JSON string representation into an object

    Args:
        my_str (str): The JSON string
    """
    return json.loads(my_str)
