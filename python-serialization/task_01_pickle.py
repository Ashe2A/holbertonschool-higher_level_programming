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

    def __init__(self, name, age, is_student):
        """
        Create the custom object.
        """

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display of object's data.
        """

        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Pickle Serialization.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print("Error:", e)

    @classmethod
    def deserialize(cls, filename):
        """
        Pickle Deserialization.
        """

        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            print("Error : file not found.")
            return None
        except UnpicklingError:
            print("Unpickling error. File might be corrupted.")
            return None
        except Exception as e:
            print("Error: {}".format(e))
            return None
