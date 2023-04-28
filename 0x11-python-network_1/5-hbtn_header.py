#!/usr/bin/python3
"""
sends a request to URL passed as argument
display the value of the header variable 'X-Request-Id'
"""

if __name__ == '__main__':
    import requests
    import sys

    try:
        res = requests.get(sys.argv[1])
        print(res.headers['X-Request-Id'])
    except Exception:
        pass
