#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Best score

    Parameters:
        a_dictionary : a dictionary

    Returns:
        Highest value key in dictionary
    """
    best_score = (list(a_dictionary))[0]
    for i in list(a_dictionary):
        if a_dictionary[i] > a_dictionary[best_score]:
            best_score = i
    return best_score
