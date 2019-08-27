#!/usr/bin/python3
"""search api"""
import requests
import sys


if __name__ == "__main__":
    part = sys.argv[1]
    if len(sys.argv) > 1:
        info = {'q': part}
    else:
        info = {'q': ""}
    re = requests.post('http://0.0.0.0:5000/search_user', data=info)
    try:
        if not re.json():
            print("No result")
        else:
            print("[{}] {}".format(re.json()['id'], re.json()['name']))
    except ValueError as err:
        print('Not a valid JSON')
