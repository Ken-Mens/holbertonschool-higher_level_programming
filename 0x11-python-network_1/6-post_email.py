#!/usr/bin/python3
""" posts email to params using post request"""

import requests
import sys

if __name__ == "__main__":
    part_a = sys.argv[1]
    part_b = sys.argv[2]
    info = {'email': part_b}
    re = requests.post(part_a, data=info)
    print(re.text)
