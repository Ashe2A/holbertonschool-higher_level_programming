#!/usr/bin/python3
"""
Pickle serialization.
"""

import pickle


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

        with open(filename, 'rb') as file:
            return cls(getattr(pickle.load(file), "name"),
                       getattr(pickle.load(file), "age"),
                       getattr(pickle.load(file), "is_student"))
