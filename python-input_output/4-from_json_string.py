#!/usr/bin/python3

"""
Returns object with a JSON info.
"""

import json


def from_json_string(my_str):
    """
    Returning the object with JSON info.
    """

    return json.loads(my_str)
