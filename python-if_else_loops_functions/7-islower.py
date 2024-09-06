#!/usr/bin/python3
def islower(c):
    """
	Check if a character is a lowercase letter.

	Parameters:
	    c (str): Character to check.
 
 	Returns:
	    bool: True if lowercase, False otherwise.
	"""
    if (len(c) == 1) and (ord('a') <= ord(c) <= ord('z')):
        return True
    return False
