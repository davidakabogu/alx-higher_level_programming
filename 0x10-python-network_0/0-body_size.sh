#!/bin/bash
# Bash script takes in a URL, sends a request, and displays the size of the response body
curl -s -I "$1" | wc -c
