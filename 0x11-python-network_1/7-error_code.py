#!/usr/bin/python3
"""
takes in a URL and sends a request
displays error code if equal or greater than 400
"""

if __name__ == '__main__':
    import sys
    import requests

    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print('Error code:', res.status_code)
    else:
        print(res.text)
