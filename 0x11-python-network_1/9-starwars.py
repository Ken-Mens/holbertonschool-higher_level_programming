#!/usr/bin/python3
""" searches for a string in star wars"""
import requests
import sys

if __name__ == "__main__":
    part_x = sys.argv[1]
    info = 'https://swapi.co/api/people/?search={}'.format(part_x)
    re = requests.get(info)
    per = re.json()
    print('Number of results: {}'.format(per['count']))
    for r in per['results']:
        print(r['name'])
