#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Sets up common elements between two sets

    Args:
        set_1 (set): First set
        set_2 (set): Second set

    Returns:
        set: The intersected set
    """
    common_set = []
    for i in set_1:
        if i in set_2:
            common_set.append(i)
    return set(common_set)
