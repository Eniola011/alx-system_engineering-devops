#!/usr/bin/python3
"""A Python Script that uses "https://jsonplaceholder.typicode.com/"
for a given employee ID, returns information about his/her TODO list progress.
extend your Python script to export data in the JSON format.
"""


import json
import requests
import sys


def export_data_json2(employee_ID):
    url = 'https://jsonplaceholder.typicode.com/'

    # fetch user details.
    usr_response = requests.get('{}/users/{}'.format(url, employee_ID))
    usr_data = usr_response.json()

    # fetch todo tasks for the user.
    todo_response = requests.get('{}/todos?userId={}'.format(url, employee_ID))
    todo_data = todo_response.json()
    tasks_dict = {}
    for usr in usr_data:
        usrname = usr.get('username')
        tasks_list = []
        for todo in todo_data:
            if usr.get('id') == todo.get('userId'):
                dicty = {'username': '', 'task': '', 'completed': None}
                tytwo = todo.get('title')
                completd = todo.get('completed')
                usrname = usr.get('username')
                dicty.update(task=tytwo, completed=completd, username=usrname)
                tasks_list.append(dicty)
                key = usr.get('id')
        tasks_dict.update({key: tasks_list})

    # json file
    with open(todo_all_employees.json, mode='w') as employee_file:
        json.dump(tasks_dict, employee_file)


if __name__ == "__main__":
    employee_ID = int(sys.argv[1])
    export_data_json2(employee_ID)
