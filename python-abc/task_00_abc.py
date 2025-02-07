#!/usr/bin/python3
"""
Abstract Animal Class and its Subclasses.
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    """Animal abstract class

    Args:
        ABC (abstract class module): abstract class module
    """

    @abstractmethod
    def sound(self):
        """
        Abstract sound of the animal
        """
        pass


class Dog(Animal):
    """Dog class

    Args:
        Animal (Animal): A dog is an animal
    """
    
    def sound(self):
        """What sound does the dog make?

        Returns:
            str: Just bark
        """
        return "Bark"


class Cat(Animal):
    """Cat class

    Args:
        Animal (Animal): A cat is an animal
    """
    
    def sound(self):
        """What sound does the cat make?

        Returns:
            str: Just meow
        """
        return "Meow"
