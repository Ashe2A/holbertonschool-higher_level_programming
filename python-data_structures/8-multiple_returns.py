#!/usr/bin/python3
def multiple_returns(sentence):
    '''Reports the length and first char of a sentence

    Args:
        sentence (str): The string

    Returns:
        tuple(int, str): The report (length and first char)
    '''
    if sentence == '':
        return (0, None)
    else:
        return (len(sentence), sentence[0])
