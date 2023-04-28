#!/usr/bin/python3
"""
takes in a letter and send a post request to 'http://0.0.0.0:5000/search_user
with letter as parameter
"""

if __name__ == '__main__':
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    val = {'q': ""}
    if len(sys.argv) > 1:
        val['q'] = sys.argv[1]

    try:
        res = requests.post(url, data=val)
        r = res.json()
        if r == {}:
            print('No result')
        else:
            print(f"[{r.get('id')}] {r.get('name')}")
    except ValueError:
        print('Not a valid JSON')
