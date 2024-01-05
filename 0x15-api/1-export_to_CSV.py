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

    print(fullList[0])
    
    with open(csv_file, 'w', newline='') as csvW:
        csv_writer = csv.writer(csvW, quoting=csv.QUOTE_ALL)

        for task in fullList:
            csv_writer.writerow([f"{userDetails.get('id')}", userDetails.get('username'), task.get('completed'), task.get('title')])
