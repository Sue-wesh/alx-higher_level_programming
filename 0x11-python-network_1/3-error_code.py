#!/usr/bin/python3
"""
takes in a URL, sends a POST request to the URL with email as parameter
and displays the body of response (decoded in utf-8)
"""
from urllib.error import HTTPError
from urllib import request, parse
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as res:
            res = res.read().decode('UTF-8')
            print(res)
    except HTTPError as exception:
        print('Error code:', exception.code)
