#!/usr/bin/python3
"""
takes in URL an email address passed as argument
sends a POST request to the URL
"""

if __name__ == '__main__':
    import sys
    import requests

    values = {'email': sys.argv[2]}
    url = sys.argv[1]
    res = requests.post(url, data=values)
    print(res.text)
