#!/usr/bin/python3
"""
Serializing and Deserializing with XML.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    json_to_xml = "<data>\n"
    for i in dictionary:
        json_to_xml += "    <{}>{}</{}>\n".format(i, dictionary[i], i)
    json_to_xml += "</data>\n"
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(json_to_xml)


def deserialize_from_xml(filename):
    xml_data = ET.parse(filename)
    root = xml_data.getroot()
    xml_to_json = {}
    for element in root:
        xml_to_json[element.tag] = element.text
    return xml_to_json
