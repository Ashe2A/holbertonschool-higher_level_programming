#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        raise TypeError("Can't instantiate abstract class Animal\
            with abstract method sound")


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"
