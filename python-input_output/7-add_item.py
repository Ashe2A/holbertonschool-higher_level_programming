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
args.pop(0)

filename = "add_item.json"
try:
    extend_json = load_from_json_file(filename)
except FileNotFoundError:
    extend_json = []
extend_json.extend(args)
save_to_json_file(extend_json, filename)
