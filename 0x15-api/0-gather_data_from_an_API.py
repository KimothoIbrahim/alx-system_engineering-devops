#!/usr/bin/python3
"""using an api"""

if __name__ == "__main__":
    import requests
    import sys

    count = 0
    newList = []
    res = requests.get(f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}")
    r = requests.get(f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos')

    for task in r.json():
        if task['completed'] == True:
            newList.append(task)
            count += 1
    
    print(f'Employee {res.json().get("name")} is done with tasks({count}/{len(r.json())}):')

    for item in newList:
        print(f'\t {item.get("title")}')
