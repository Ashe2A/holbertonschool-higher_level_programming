#!/usr/bin/python3
'''CountedIterator - Keeping Track of Iteration'''


class CountedIterator():
    '''Counted iterator class'''

    def __init__(self, some_iterable):
        '''Counted iterator constructor

        Args:
            some_iterable (Iterable): an iterable type
        '''
        self.__iterator = iter(some_iterable)
        self.__counter = 0

    def __next__(self):
        '''Iterate the iterable

        Raises:
            StopIteration: when the iterable is on the edge

        Returns:
            iteration: the next iteration
        '''
        try:
            next_iteration = next(self.__iterator)
        except StopIteration as e:
            raise StopIteration(e)
        self.__counter += 1
        return next_iteration

    def get_count(self):
        '''Get the number of iterations passed through

        Returns:
            int: the number of iterations
        '''
        return self.__counter
