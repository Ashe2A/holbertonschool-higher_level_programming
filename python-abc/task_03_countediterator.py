#!/usr/bin/env python3
"""
Counted Iterator
"""


class CountedIterator():
    """
    Updated talkative list
    """

    def __init__(self, some_iterable):
        self.iterator = iter(some_iterable)
        self.counter = 0
    
    def get_count(self):
        return self.counter

    def __next__(self):
        try:
            self.counter += 1
            return next(self.iterator)
        except StopIteration:
            raise StopIteration()

    def __iter__(self):
        return self
