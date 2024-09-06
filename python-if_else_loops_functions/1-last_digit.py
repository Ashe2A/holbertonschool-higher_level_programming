#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    number_mod = -number
number_mod = number % 10
print(f"Last digit of {number} is {number_mod} and is " +
      ("greater than 5" if (number_mod) > 5 else
       ("0" if (number_mod) == 0 else "less than 6 and not 0")))
