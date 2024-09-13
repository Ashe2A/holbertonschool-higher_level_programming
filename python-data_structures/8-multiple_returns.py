#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Length and first character of a string.

    Parameters:
        sentence (string) : the string.

    Returns:
        Tuple (int, int/string) : the length and the first character
    """
    if (len(sentence) == 0):
        return (0, "None")
    return (len(sentence), sentence[0])
