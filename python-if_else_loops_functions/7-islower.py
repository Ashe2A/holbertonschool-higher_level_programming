#!/usr/bin/python3
def islower(c):
    """
	Check if a character is a lowercase letter.

	Parameters:
	    c (int): Character to check.
 
 	Returns:
	    bool: True if lowercase, False otherwise.
	"""
    if ord('a') <= c <= ord('z'):
        return True
    return False
