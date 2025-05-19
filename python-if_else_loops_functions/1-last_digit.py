#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
moduloten = abs(number) % 10
if number < 0:
    moduloten = -moduloten
print('Last digit of {} is {} and is '.
      format(number, moduloten), end='')
if moduloten > 5:
    print('greater than 5')
elif moduloten == 0:
    print('0')
else:
    print('less than 6 and not 0')
