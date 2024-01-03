#!/usr/bin/python3
"""A Python Script that uses "https://jsonplaceholder.typicode.com/"
for a given employee ID, returns information about his/her TODO list progress.
extend your Python script to export data in the CSV format.
"""


import csv
import requests
import sys


def export_data_csv(employee_ID):
    url = 'https://jsonplaceholder.typicode.com/'

    # fetch user details.
    usr_response = requests.get('{}/users/{}'.format(url, employee_ID))
    usr_data = usr_response.json()
    usrname = usr_data.get('username')

    # fetch todo tasks for the user.
    todo_response = requests.get('{}/todos?userId={}'.format(url, employee_ID))
    todo_data = todo_response.json()
    tasks = []
    for task in todo_data:
        tasks.append([employee_ID, usrname, task.get('completed'),
                     task.get('title')])
    # csv file
    csvfile = '{}.csv'.format(employee_ID)
    with open(csvfile, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        for task in tasks:
            employee_writer.writerow(task)


if __name__ == "__main__":
    employee_ID = int(sys.argv[1])
    export_data_csv(employee_ID)
