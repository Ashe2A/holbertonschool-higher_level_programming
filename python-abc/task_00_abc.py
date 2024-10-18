#!/usr/bin/python3
"""
Animal classes
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Animal abstract class
    """

    @abstractmethod
    def sound(self):
        """
        Animal's sound
        """

        raise Exception("sound() is not implemented")


class Dog(Animal):
    """
    Dog class
    """

    def sound(self):
        """
        Dog's sound
        """

        return "Bark"


class Cat(Animal):
    """
    Cat class
    """

    def sound(self):
        """
        Cat's sound
        """

        return "Meow"
