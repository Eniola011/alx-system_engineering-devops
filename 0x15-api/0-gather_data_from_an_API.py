#!/usr/bin/python3
"""A Python Script that uses "https://jsonplaceholder.typicode.com/"
for a given employee ID, returns information about his/her TODO list progress.
"""


import requests
import sys


def employee_todo_progress(employee_ID):
    url = 'https://jsonplaceholder.typicode.com/'

    usr_response = requests.get('{}/users/{}'.format(url, employee_ID))
    usr_data = usr_response.json()

    todo_response = requests.get('{}/todos?userId={}'.format(url, employee_ID))
    todo_data = todo_response.json()

    tasks = len(todo_data)
    task = sum(task['completed'] for task in todo_data)

    print('Employee {} is done with tasks({}/{})'.format
          (usr_data['name'], task, tasks))
    for task in todo_data:
        if task['completed']:
            print("\t{}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_ID>")
        sys.exit(1)

    employee_ID = int(sys.argv[1])
    employee_todo_progress(employee_ID)
