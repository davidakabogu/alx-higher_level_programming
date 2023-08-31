#!/usr/bin/env bash
# Bash script takes in a URL, sends a request, and displays the size of the response body
curl -sI "$1" | wc -c
