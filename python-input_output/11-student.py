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

    def to_json(self, attrs=None):
        """JSON Student with only the attributes

        Args:
            attrs (list[str], optional): Attribute names. Defaults to None.

        Returns:
            dict: dictionnary of the Student instance
        """
        json_student = {}
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            for i in attrs:
                if i in self.__dict__:
                    json_student[i] = self.__dict__[i]
            return json_student
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for i in json:
            self.__dict__[i] = json[i]
