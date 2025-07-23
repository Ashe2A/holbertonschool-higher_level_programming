#!/usr/bin/python3
s1 = "Best School"
s2 = "Best School"

with open("9-answer.txt", "w") as f:
    """If s1 and s2 are the same object,
    write True in 9-answer.txt, otherwise False"""
    f.write("{}\n".format(s1 is s2))
