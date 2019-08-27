#!/usr/bin/python3
""" pings github """

import requests
from requests.auth import HTTPBasicAuth
import sys
if __name__ == "__main__":
    part_x = sys.argv[1]
    part_y = sys.argv[2]
    re = requests.get('https://api.github.com/users/' + part_x,
                      auth=HTTPBasicAuth(part_x, part_y))
    print(re.json().get('id'))
