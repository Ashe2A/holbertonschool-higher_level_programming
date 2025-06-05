#!/usr/bin/python3
'''Load, add, save'''
from sys import argv
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

item_list = []
if path.isfile('add_item.json'):
    item_list.extend(load_from_json_file('add_item.json'))
for i in range(1, len(argv)):
    item_list.append(argv[i])
save_to_json_file(item_list, 'add_item.json')
