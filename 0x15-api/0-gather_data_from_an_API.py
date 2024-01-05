#!/usr/bin/python3
"""using an api"""

if __name__ == "__main__":
    import requests
    import sys

    userid = sys.argv[1]

    res = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{userid}")
    r = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{userid}/todos')

    userDetails = res.json()
    fullList = r.json()

    newList = [task for task in fullList if task['completed']]

    print(
        f'Employee {userDetails.get("name")} is \
        done with tasks({len(newList)}/{len(fullList)}): ')

    for item in newList:
        print(f'\t {item.get("title")}')
