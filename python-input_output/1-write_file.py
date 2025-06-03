#!/usr/bin/python3
'''Write to a file'''


def write_file(filename='', text=''):
    '''Write a file of a filename

    Args:
        filename (str, optional): Name of the file. Defaults to empty string.
        text (str, optional): Text to write. Defaults to empty string.
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
