#!/usr/bin/python3
def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    tmp = list(text)
    for x in range(len(tmp)):
        try:
            if tmp[x] == '.' or tmp[x] == '?' or tmp[x] == ':':
                tmp.insert(x + 1, '\n')
        except:
            pass

    tmp = "".join(tmp).split('\n')
    for x in tmp:
        print(x.strip())
        print()
