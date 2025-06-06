#!/usr/bin/python3
"""Extending the Python List with Notifications"""


class VerboseList(list):
    """Verbost list class

    Args:
        list (class): Inherits from built-in type list
    """

    def append(self, object):
        """Append overriding class"""
        super().append(object)
        print("Added [{}] to the list.".format(object))

    def extend(self, iterable):
        """Extend overriding class"""
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, value):
        """Remove overriding class"""
        print("Removed [{}] from the list.".format(value))
        super().remove(value)

    def pop(self, index=-1):
        """Pop overriding class"""
        popped_item = self[index]
        print("Popped [{}] from the list.".format(popped_item))
        return super().pop(index)
