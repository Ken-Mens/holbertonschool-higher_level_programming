#!/usr/bin/python3
def max_integer(my_list=[]):
    if not len(my_list):
        return (None)
    else:
        foo = my_list[0]
        for idx in my_list:
            if idx >= foo:
                foo = idx
    return (foo)
