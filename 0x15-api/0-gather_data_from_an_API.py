#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = request.get('{}/users/{}'.format(url, employee_id)).json()
    user_name = user.get('name')
    completed_tasks = []
    total_task = requests.get('{}/todos?userId={}'.format(url,
                                                          employee_id)).json()
    for task in total_task:
        if task["completed"] is True:
            completed_task.append(task['title'])

    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, len(completed_task), len(total_task)))

    for task in completed_task:
        print('\t{}'.format(task))
