#!/bin/bash
#only status code
curl -s -o $1/dev/null -w "%{http_code}" $1
