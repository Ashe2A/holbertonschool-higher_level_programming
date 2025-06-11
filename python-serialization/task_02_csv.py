#!/usr/bin/python3
"""Converting CSV Data to JSON Format"""
import csv

def convert_csv_to_json(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            csv_data = csv.DictReader(f)
            dict_list = []
            for i in csv_data:
                dict_list.append(i)
        with open("data.json", "w", encoding="utf-8") as f:
            f.write("{}".format(dict_list).replace("\'", "\""))
        return True
    except Exception as e:
        print(e)
        return False
