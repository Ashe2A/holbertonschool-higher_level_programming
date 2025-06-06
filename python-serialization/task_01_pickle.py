#!/usr/bin/python3
"""Pickling Custom Classes"""
import pickle


class CustomObject():
    """Custom class"""

    def __init__(self, name, age, is_student):
        """Custom constructor

        Args:
            name (str): Name of the object (?)
            age (str): Age of the object (?)
            is_student (bool): True if object is student, False otherwise
        """
        try:
            self.name = name
            self.age = age
            self.is_student = is_student
        except Exception as e:
            print(e)

    def display(self):
        """Display info of the object"""
        try:
            print("Name: {}".format(self.name))
            print("Age: {}".format(self.age))
            print("Is Student: {}".format(self.is_student))
        except Exception as e:
            print(e)

    def serialize(self, filename):
        """Serialize the object into a pickle file

        Args:
            filename (str): The pickle file name
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception as e:
            print(e)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a pickle file to create an instance

        Args:
            filename (str): The pickle file name

        Returns:
            CustomObject: The new deserialized instance
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception as e:
            print(e)
            return None
