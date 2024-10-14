#!/usr/bin/python3
"""
Serializing and Deserializing with XML.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    json_to_xml = "<data>"
    for i in dictionary:
        json_to_xml += "<{}>{}</{}>".format(i, dictionary[i], i)
    json_to_xml += "</data>"
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(json_to_xml)

def deserialize_from_xml(filename):
    xml_data = ET.parse(filename)
    xml_to_json = {}
    for i in xml_data:
        xml_to_json[i] = xml_data[i]
