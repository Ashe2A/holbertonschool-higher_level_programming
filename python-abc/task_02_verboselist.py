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
            print(f"Added [{item}] to the list.")

    def extend(self, x):
        """
        Extends a list with another one

        Parameters:
            self: the list to extend
            x: the list to append
        """
        if not (x is None):
            super().extend(x)
            print(f"Extended the list with [{x}] items.")

    def remove(self, item):
        """
        Removes an item to the list

        Parameters:
            self: the list
            item: the item to remove
        """
        if item in self:
            super().remove(item)
            print(f"Removed [{item}] from the list.")

    def pop(self, item):
        """
        Pops an item to the list

        Parameters:
            self: the list
            item: the index of the item to pop
        """
        if 0 <= item <= len(self) - 1:
            super().pop(item)
            print(f"Popped [{item}] from the list.")

    def pop(self):
        """
        Pops the last item to the list

        Parameters:
            self: the list
        """
        super().pop(len(self) - 1)
        print(f"Popped [{self[len(self) - 1]}] from the list.")
