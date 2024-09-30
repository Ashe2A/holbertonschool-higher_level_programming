#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding="utf-8") as file:
        try:
            read_data = file.read()
        except FileNotFoundError:
            print("file doesn't exist")
        except PermissionError:
            print("file permission")
        print(read_data)
