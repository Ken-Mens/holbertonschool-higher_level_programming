#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, 'a', encoding='UTF-8') as foo:
        return foo.write(text)
