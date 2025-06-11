#!/usr/bin/python3
"""Serializing and Deserializing with XML"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary tree into an XML file

    Args:
        dictionary (dict): Dictionary tree
        filename (str): The XML file to write
    """
    root = ET.Element("data")
    for i in dictionary:
        element = ET.Element(i)
        element.text = dictionary[i]
        root.append(element)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize an XML file into a dictionary tree

    Args:
        filename (str): The name of the XML file

    Returns:
        dict: The corresponding dictionary tree
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    xml_dic = {}
    for i in root:
        xml_dic[i.tag] = i.text
    return xml_dic
