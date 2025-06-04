#!/usr/bin/python3
'''Append to a file'''


def append_write(filename='', text=''):
    '''Write a file of a filename by appending  

    Args:
        filename (str, optional): Name of the file. Defaults to empty string.
        text (str, optional): Text to write. Defaults to empty string.
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
