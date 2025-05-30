#!/usr/bin/python3
'''Abstract Animal Class and its Subclasses'''
from abc import ABC
from abc import abstractmethod


class Animal(ABC):
    '''Animal abstract class

    Args:
        ABC (class): Inherits from bstract class
    '''

    @abstractmethod()
    def sound():
        '''Sound abstract method

        Raises:
            TypeError: If subclasses don't implement the method
        '''
        raise TypeError('Can\'t instantiate abstract class Animal with\
            abstract method sound')


class Dog(Animal):
    '''Dog class'''

    def sound():
        '''Dog sound method

        Returns:
            str: A dog barks
        '''
        return 'Bark'


class Cat(Animal):
    '''Cat class'''

    def sound():
        '''Car sound method

        Returns:
            str: A cat meows
        '''
        return 'Meow'
