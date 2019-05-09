#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = {}
    for i in my_dict.items():
        new_dict[i] = i * 2
    return new_dict
