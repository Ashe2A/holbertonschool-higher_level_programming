#!/usr/bin/python3
'''CountedIterator - Keeping Track of Iteration'''


class CountedIterator():
    def __init__(self, some_iterable):
        self.__iterator = iter(some_iterable)
        self.__counter = 0

    def __next__(self):
        try:
            next_iteration = next(self.__iterator)
        except StopIteration as e:
            print(e)
        self.__counter += 1
        return next_iteration

    def get_count(self):
        return self.__counter
