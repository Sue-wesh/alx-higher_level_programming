#!/usr/bin/python3
"""
takes in a URL, sends a POST request to the URL with email as parameter
and displays the body of response (decoded in utf-8)
"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values).encode('utf-8')

    url = sys.argv[1]

    resp = request.Request(url, data)
    with request.urlopen(resp) as response:
        print(response.read().decode('utf-8'))
