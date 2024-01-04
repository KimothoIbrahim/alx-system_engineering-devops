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
    
    with open(csv_file, 'w', newline='') as csvW:
        csv_writer = csv.writer(csvW)

        for task in fullList:
            csv_writer.writerow([f'{userid}', f'{userDetails.get("name")}', f'{task.get("completed")}', f'{task.get("title")}'])
