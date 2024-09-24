#!/usr/bin/env python3
"""
Extending lists
"""


class VerboseList(list):
    """
    Updated talkative list
    """

    def append(self, item):
        if not (item is None):
            super().append(item)
            print(f"Added [{item}] to the list.")

    def extend(self, x):
        if not (x is None):
            super().extend(x)
            print(f"Extended the list with [{x}] items.")

    def remove(self, item):
        if item in self:
            super().remove(item)
            print(f"Removed [{item}] from the list.")

    def pop(self, item):
        if 0 <= pop <= len(self) - 1:
            super().pop(item)
            print(f"Popped [item] from the list.")
