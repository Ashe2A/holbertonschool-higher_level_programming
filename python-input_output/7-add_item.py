#!/usr/bin/python3

"""
Loads object from JSON file.
"""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
append_write = __import__('2-append_write').append_write
from_json_string = __import__('4-from_json_string').from_json_string
import sys

args = []
for i in sys.argv:
    args.append(i)
args.pop(0)

filename = "add_item.json"
new_json = append_write(filename, args)
save_to_json_file(load_from_json_file(filename), filename)
