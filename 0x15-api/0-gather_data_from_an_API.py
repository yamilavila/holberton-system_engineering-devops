#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
from sys import argv


if __name__ == '__main__':

    employee_id = argv[1]
    user = request.get('https://jsonplaceholder.typicode.com/users/{}'
                       .format(employee_id))

    name_employee = user.jason()['name']
    todo = request.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                       .format(employee_id))

    todo = todo.json()

    num_done_task = 0
    task_list = []

    for task in todo:
        if task["completed"] is True:
            num_done_task += 1
            task_list.append(task['title'])

    print("Employee {} is done with tasks({}/{}):"
          .format(name_employee, num_done_task, len(todo)))

    for done in range(len(task_list)):
        print("\t {}".format(task_list[done]))
