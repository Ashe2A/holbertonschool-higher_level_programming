#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """Indents text by characters

    Args:
        text (str): The text to indent

    Raises:
        TypeError: If text isn't a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print()
            print()
            while text[i + 1] == " ":
                i += 1
        i += 1
