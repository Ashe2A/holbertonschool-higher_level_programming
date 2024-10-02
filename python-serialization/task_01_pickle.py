#!/usr/bin/python3
"""
Pickle serialization.
"""

import pickle
import os


class CustomObject:
    """
    Custom object.
    """

    def __init__(self, name="", age=0, is_student=False):
        """
        Create the custom object.
        """

        self.__name = name
        self.__age = age
        self.__is_student = is_student

    def display(self):
        """
        Display of object's data.
        """

        print("Name: {}".format(self.__name))
        print("Age: {}".format(self.__age))
        print("Is Student: {}".format(self.__is_student))

    def serialize(self, filename):
        """
        Pickle Serialization.
        """

        with open(filename, 'wb') as file:
            pickle.dump(self.__dict__, file)

    @classmethod
    def deserialize(cls, filename):
        """
        Pickle Deserialization.
        """

        if not os.path.exists(filename):
            return None
        else:
            with open(filename, 'rb') as file:
                loaded_file = pickle.load(file)
                cls_name = "_{}".format(cls.__name__)
                return cls(loaded_file.get(cls_name + "__name", ""),
                           loaded_file.get(cls_name + "__age", 0),
                           loaded_file.get(cls_name + "__is_student", True))
