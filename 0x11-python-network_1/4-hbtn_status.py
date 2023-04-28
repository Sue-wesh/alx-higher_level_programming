#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
uses 'requests' package
"""

if __name__ == '__main__':
    import requests

    res = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type:', type(res.text))
    print('\t- content:', res.text)
