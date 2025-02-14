#!/usr/bin/python3

"""
Returns object with a JSON info.
"""

import json


def from_json_string(my_str):
    """
    Returning the object with JSON info.

    Parameters:
        my_obj: object containing json content

    Returns:
        The original object
    """

    return json.loads(my_str)
