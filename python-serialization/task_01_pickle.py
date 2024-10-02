#!/usr/bin/python3
"""
Pickle serialization.
"""

import pickle
from pickle import UnpicklingError


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
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self.__dict__, file)
        except Exception as e:
            print("Error:", e)

    @classmethod
    def deserialize(cls, filename):
        """
        Pickle Deserialization.
        """

        try:
            with open(filename, 'rb') as file:
                unpickle = pickle.load(file)
                cls_name = "_{}".format(cls.__name__)
                name = unpickle.get("{}__name".format(cls_name), "")
                age = unpickle.get("{}__age".format(cls_name), 0)
                is_student = unpickle.get("{}__is_student".format(cls_name),
                                          False)
                return cls(name, age, is_student)
        except FileNotFoundError:
            print("Error : file not found.")
            return None
        except UnpicklingError:
            print("Unpickling error.")
            return None
        except Exception as e:
            print("Error:", e)
            return None
