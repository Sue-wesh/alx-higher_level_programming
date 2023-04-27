#!/usr/bin/env bash
# takes in a URL, send request to it and display size of body of response

curl -s "$1" | wc -c
