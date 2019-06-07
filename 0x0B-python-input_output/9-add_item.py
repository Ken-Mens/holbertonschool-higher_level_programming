#!/usr/bin/python3
import json
import sys
import stat

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = 'add_item.json'

try:
    newlist = load_from_json_file(filename)
except (FileNotFoundError):
    newlist = []

for y in sys.argv[1:]:
    newlist.append(y)

save_to_json_file(newlist, filename)
