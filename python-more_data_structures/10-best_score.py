#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    max_key = ""
    if a_dictionary == {} or a_dictionary is None:
        return None
    else:
        for i in a_dictionary:
            if a_dictionary[i] >= max:
                max = a_dictionary[i]
                max_key = i
        return max_key
