#!/usr/bin/python3
"""Making a csv"""

if __name__ == "__main__":
    import csv
    import json
    import requests
    import sys

    response = requests.get(
        'https://jsonplaceholder.typicode.com/users')
    r = requests.get(
        f'https://jsonplaceholder.typicode.com/todos')

    fullList = r.json()
    users = response.json()

    new_grouped_tasks = {}

    for task in fullList:
        if task['userId'] not in new_grouped_tasks:
            new_grouped_tasks[task['userId']] = []
        for user in users:
            if user['id'] == task['userId']:
                new_grouped_tasks[task['userId']].append(
                        {'username': user['username'],
                            'task': task['title'],
                            'completed': task['completed']})

    with open('todo_all_employees.json', 'w', encoding='utf-8') as all_json:
        json.dump(new_grouped_tasks, all_json)
