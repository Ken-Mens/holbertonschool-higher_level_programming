#!/bin/bash
#Curl only methods that takes in URL and displays all HTTP
curl -sI "$1" | grep Allow | cut -d ' ' -f2-
