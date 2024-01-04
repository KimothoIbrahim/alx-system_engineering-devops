#!/usr/bin/python3
"""Making a csv"""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    userid = sys.argv[1]

    res = requests.get(f"https://jsonplaceholder.typicode.com/users/{userid}")
    r = requests.get(f'https://jsonplaceholder.typicode.com/users/{userid}/todos')

    userDetails = res.json()
    fullList = r.json()
    csv_file = f'{userid}.csv'

    print(userDetails)
    
    with open(csv_file, 'w', newline='') as csvW:
        csv_writer = csv.writer(csvW)

        for task in fullList:
            csv_writer.writerow([userDetails.get("id"), userDetails.get('username'), task.get("completed"), task.get("title")])
