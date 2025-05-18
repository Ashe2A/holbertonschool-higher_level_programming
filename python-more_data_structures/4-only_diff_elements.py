#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Sets up unique elements between two sets

    Args:
        set_1 (set): First set
        set_2 (set): Second set

    Returns:
        set: The union set
    """
    diff_set = []
    for i in set_1:
        if i not in set_2:
            diff_set.append(i)
    for i in set_2:
        if i not in set_1:
            diff_set.append(i)
    return set(diff_set)
