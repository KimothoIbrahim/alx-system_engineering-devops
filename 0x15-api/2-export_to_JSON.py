#!/usr/bin/python3
"""Making a csv"""

if __name__ == "__main__":
    import csv
    import json
    import requests
    import sys

    userid = sys.argv[1]

    res = requests.get(f"https://jsonplaceholder.typicode.com/users/{userid}")
    r = requests.get(f'https://jsonplaceholder.typicode.com/users/{userid}/todos')

    userDetails = res.json()
    fullList = r.json()
    json_file = f'{userid}.json'

    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        json.dump({userDetails.get('id'): fullList}, jsonfile)
