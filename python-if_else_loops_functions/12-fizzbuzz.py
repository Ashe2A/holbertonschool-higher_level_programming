#!/usr/bin/python3
def fizzbuzz():
    for i in range(100 + 1):
        whatnum = ""
        if i % 3 == 0:
            whatnum += "Fizz"
        if i % 5 == 0:
            whatnum += "Buzz"
        if whatnum == "":
            whatnum = i
        print(whatnum, end=" ")
