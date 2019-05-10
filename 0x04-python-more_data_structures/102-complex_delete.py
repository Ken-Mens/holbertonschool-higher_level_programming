#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary.copy()
    for val in new_dict:
        if new_dict[val] == value:
            del a_dictionary[val]
    return a_dictionary
