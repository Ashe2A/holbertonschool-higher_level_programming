#!/usr/bin/python3
"""
Converting CSV Data to JSON Format.
"""

import csv
import json
from csv import Error


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, encoding="utf-8") as csv_file:
            csv_data = csv.DictReader(csv_file)
        with open("data.json", 'w', encoding="utf-8") as json_file:
            json_file.write(json.dumps(csv_data))
        return True
    except FileNotFoundError:
        print("Error : file not found.")
        return False
    except Error:
        print("CSV dictionary reading error")
        return False
