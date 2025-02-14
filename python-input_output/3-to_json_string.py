#!/usr/bin/python3

"""
Returns JSON info of string.
"""

import json


def to_json_string(my_obj):
    """
    Returning the JSON info of string.

    Parameters:
        my_obj: object containing json content

    Returns:
        The JSON info of the object
    """

    return json.dumps(my_obj)
