#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Best score

    Parameters:
        a_dictionary : a dictionary

    Returns:
        Highest value key in dictionary
    """
    if a_dictionary == {}:
        return "None"
    best_scorer = ""
    for i in list(a_dictionary):
        if a_dictionary[i] > a_dictionary[best_scorer]:
            best_scorer = i
    return best_scorer
