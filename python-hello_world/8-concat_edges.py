#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = f"{str[39:67]}" + f"{str[-22:-17]}" + f"{str[:6]}"
print(str)
