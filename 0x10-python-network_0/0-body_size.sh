#!/bin/bash
# Bash script takes in a URL, sends a request and displays size of response body
curl -s "$1" | wc -c
