#!/usr/bin/python3
"""A Python Script that uses "https://jsonplaceholder.typicode.com/"
for a given employee ID, returns information about his/her TODO list progress.
"""


import requests
import sys


def employee_todo_progress(employee_ID):
    url = 'https://jsonplaceholder.typicode.com/'

    # fetch user details.
    usr_response = requests.get('{}/users/{}'.format(url, employee_ID))
    usr_data = usr_response.json()
    usrname = usr_data.get("name")
    sumtotal = 0
    sumcount = 0

    # fetch todo tasks for the user.
    todo_response = requests.get('{}/todos?userId={}'.format(url, employee_ID))
    todo_data = todo_response.json()

    # calculate user's progress on tasks.
    tasks = []
    for task in todo_data:
        sumtotal += 1
        if task.get('completed') is True:
            tasks.append(task)
            sumcount += 1

    # display user's progress on tasks.
    print('Employee {} is done with tasks({}/{}):'.format
          (usrname, sumcount, sumtotal))
    # display user's completed tasks
    for task in tasks:
        print("\t{}".format(task.get("title")))


if __name__ == "__main__":
    employee_ID = int(sys.argv[1])
    employee_todo_progress(employee_ID)
