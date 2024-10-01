#!/usr/bin/python3
"""
Student.
"""


class Student:

    """
    Student class.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            dict_only_str = {}
            for i in attrs:
                if isinstance(i, str) and hasattr(self, i):
                    dict_only_str[i] = getattr(self, i)
            return dict_only_str
        else:
            return self.__dict__

    def reload_from_json(self, json):
        if isinstance(json, list):
            self.__dict__ = json
