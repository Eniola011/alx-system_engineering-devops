#!/usr/bin/python3
"""A Python Script that uses "https://jsonplaceholder.typicode.com/"
for a given employee ID, returns information about his/her TODO list progress.
extend your Python script to export data in the CSV format.
"""


import requests
import sys
import csv


def employee_todo_progress(employee_ID):
    url = 'https://jsonplaceholder.typicode.com/'

    # fetch user details.
    usr_response = requests.get('{}/users/{}'.format(url, employee_ID))
    usr_data = usr_response.json()

    # fetch todo tasks for the user.
    todo_response = requests.get('{}/todos?userId={}'.format(url, employee_ID))
    todo_data = todo_response.json()

    # csv file
    csvfile = '{}.csv'.format(employee_ID)

    # transfer infor into csv file.
    with open(csvfile, mode='w', newline='') as employee_file:
        fieldnames = ["USER_ID", "USERNAME",
                   "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        employee_writer = csv.DictWriter(employee_file, fieldnames=fieldnames)
        # write header.
        employee_writer.writeheader()
        # write tasks.
        for task in todo_data:
            employee_writer.writerow({
                'USER_ID': employee_ID,
                'USERNAME': usr_data['username'],
                'TASK_COMPLETED_STATUS': 'True'
                if task['completed'] else 'False',
                'TASK_TITLE': task['title']
            })

    print('Data exported to {}'.format(csvfile))


if __name__ == "__main__":
    employee_ID = int(sys.argv[1])
    employee_todo_progress(employee_ID)
