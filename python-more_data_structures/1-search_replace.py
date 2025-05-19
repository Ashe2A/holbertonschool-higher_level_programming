#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''Search and replace elements in a list

    Args:
        my_list (list): The list
        search (obj): The element to search for
        replace (obj): The replacing element

    Returns:
        list: The new modified list
    '''
    new_list = []
    for i in my_list:
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)
    return new_list
