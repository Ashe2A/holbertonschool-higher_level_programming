#!/usr/bin/python3
"""The Mystical Dragon - Mastering Mixins"""


class SwimMixin():
    """Swimming creature class"""

    def swim(self):
        """Make the creature swim"""
        print("The creature swims!")


class FlyMixin():
    """Flying creature class"""

    def fly(self):
        """Make the creature fly"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class

    Args:
        SwimMixin (obj): Inherits from swimming creatures
        FlyMixin (obj): Inherits from flying creatures
    """

    def roar(self):
        """Dragons also roar"""
        print("The dragon roars!")
