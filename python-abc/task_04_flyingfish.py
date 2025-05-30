#!/usr/bin/python3
'''The Enigmatic FlyingFish - Exploring Multiple Inheritance'''


class Fish():
    '''Fish class'''

    def swim(self):
        '''Fishes swim'''
        print('The fish is swimming')

    def habitat(self):
        '''Fishes live in water'''
        print('The fish lives in water')


class Bird():
    '''Bird class'''

    def fly(self):
        '''Birds fly'''
        print('The bird is flying')

    def habitat(self):
        '''Birds live in the sky (which is not accurate)'''
        print('The bird lives in the sky')


class FlyingFish(Fish, Bird):
    '''Flying fish class

    Args:
        Fish (obj): Inherits from fishes
        Bird (obj): Inherits from birds
    '''

    def fly(self):
        '''Flying fishes soar'''
        print('The flying fish is soaring!')

    def swim(self):
        '''Flying fishes swim'''
        print('The flying fish is swimming!')

    def habitat(self):
        '''Flying fishes live in water and sky (which is not accurate)'''
        print('The flying fish lives both in water and the sky!')
