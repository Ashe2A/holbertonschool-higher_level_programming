#!/usr/bin/python3
"""
Text indentation.
Usage: text_indentation(text)
"""


def text_indentation(text):
    """
    Indents a text with newlines after "?", "." or ":".

    Params:
        text: The text
    """

    new_text = ""
    new_line = True
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        for i in text:
            if not (i == " " and new_line):
                new_text += i
            if i == "." or i == "?" or i == ":":
                new_text += "\n\n"
                new_line = True
            else:
                new_line = False
    print(new_text, end="")
