#!/usr/bin/python3
def best_score(a_dictionary):
    """Gets the highest value"s key in a dictionary

    Args:
        a_dictionary (dict): The dictionary

    Returns:
        string: The corresponding key, None if there is none
    """
    if a_dictionary is not None and a_dictionary != {}:
        max = None
        for i in a_dictionary:
            if max is None or a_dictionary[i] > max:
                max = a_dictionary[i]
                best = i
        return best
