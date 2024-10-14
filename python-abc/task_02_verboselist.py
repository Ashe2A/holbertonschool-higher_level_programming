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
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """
        Extends a list with another one

        Parameters:
            self: the list to extend
            x: the list to append
        """
        super().extend(x)
        print("Extended the list with [{}] items.".format(len(x)))

    def remove(self, item):
        """
        Removes an item to the list

        Parameters:
            self: the list
            item: the item to remove
        """
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, idx=-1):
        """
        Pops an item to the list

        Parameters:
            self: the list
            item: the index of the item to pop
        """
        item = super().pop(idx)
        print("Popped [{}] from the list.".format(item))
        return item
