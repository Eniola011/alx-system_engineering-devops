#!/usr/bin/python3
"""A Python Script that uses "https://jsonplaceholder.typicode.com/"
for a given employee ID, returns information about his/her TODO list progress.
extend your Python script to export data in the JSON format.
"""


import json
import requests
import sys


def export_data_json(employee_ID):
    url = 'https://jsonplaceholder.typicode.com/'

    # fetch user details.
    usr_response = requests.get('{}/users/{}'.format(url, employee_ID))
    usr_data = usr_response.json()
    usrname = usr_data.get('username')

    # fetch todo tasks for the user.
    todo_response = requests.get('{}/todos?userId={}'.format(url, employee_ID))
    todo_data = todo_response.json()
    tasks_dict = {}
    tasks_list = []
    for todo in todo_data:
        dicty = {'task': '', 'completed': None, 'username': usrname}
        tytwo = todo.get('title')
        completd = todo.get('completed')
        dicty.update(task=tytwo, completed=completd)
        tasks_list.append(dicty)
    tasks_dict.update({employee_ID: tasks_list})

    # json file
    jsonfile = '{}.json'.format(employee_ID)
    with open(jsonfile, mode='w') as employee_file:
        json.dump(tasks_dict, employee_file)


if __name__ == "__main__":
    employee_ID = int(sys.argv[1])
    export_data_json(employee_ID)
