#!/usr/bin/python3
"""Student to JSON"""


class Student():
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Student class constructor

        Args:
            first_name (str): Student's first name
            last_name (str): Student's last name
            age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """JSON Student

        Returns:
            dict: dictionnary of the Student instance
        """
        return self.__dict__
