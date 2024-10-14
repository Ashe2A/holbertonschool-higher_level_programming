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
            next_iter = next(self.iterator)
            self.counter += 1
            return next_iter
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        return self
