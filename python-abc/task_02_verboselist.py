#!/usr/bin/env python3
"""
Extending lists
"""


class VerboseList(list):
    """
    Updated talkative list
    """

    def append(self, item):
        """
        Appends an item to the list

        Parameters:
            self: the list
            item: the item to append
        """
        if not (item is None):
            super().append(item)
            print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """
        Extends a list with another one

        Parameters:
            self: the list to extend
            x: the list to append
        """
        if not (x is None):
            super().extend(x)
            print("Extended the list with [{}] items.".format(x))

    def remove(self, item):
        """
        Removes an item to the list

        Parameters:
            self: the list
            item: the item to remove
        """
        if item in self:
            super().remove(item)
            print("Removed [] from the list.".format(item))

    def pop(self, item):
        """
        Pops an item to the list

        Parameters:
            self: the list
            item: the index of the item to pop
        """
        if 0 <= item <= len(self) - 1:
            super().pop(item)
            print("Popped [{}] from the list.".format(item))

    def pop(self):
        """
        Pops the last item to the list

        Parameters:
            self: the list
        """
        super().pop(len(self) - 1)
        print("Popped [{}] from the list.".format(self[len(self) - 1]))
