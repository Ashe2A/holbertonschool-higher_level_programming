#!/usr/bin/python3

"""
Loads object from JSON file.
"""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys

args = []
for i in sys.argv:
    args.append(i)

with open("add_item.json", 'w', encoding="utf-8") as file:
    file.write(args)
