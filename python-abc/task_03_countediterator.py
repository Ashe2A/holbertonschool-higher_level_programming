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
    
    @property
    def get_count(self):
        return self.counter

    def __next__(self, iterable):
        if self.counter >= len(self.iterator) - 1:
            raise StopIteration()
        else:
            print(iterable[self.counter])
            self.counter += 1
