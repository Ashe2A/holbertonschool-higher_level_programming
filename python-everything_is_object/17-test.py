#!/usr/bin/python3
"""Tests for List incrementation"""
def increment(n):
    n.append(4)


l_disambig = [1, 2, 3]
increment(l_disambig)

with open("17-answer.txt", "w") as f:
    """Print a (check whether l has been appended with 4 using a method)
    in 17-answer.txt"""
    f.write("{}\n".format(l_disambig))
