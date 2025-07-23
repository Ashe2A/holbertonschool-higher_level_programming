#!/usr/bin/python3
def magic_string(_iteration=[0]):
    _iteration[0] += 1
    return ", ".join("BestSchool" for i in range(_iteration[0]))
