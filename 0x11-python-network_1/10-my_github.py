#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password) 
and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys

    basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    res = requests.get('https://api.github.com/user', auth=basic)
    res = res.json()
    print(res.get('id'))
