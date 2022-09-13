#!/usr/bin/python3
"""Export to CSV"""
import csv
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get('{}/users/{}'.format(url, employee_id)).json()
    user_name = user.get('name')
    tasks_completed = []
    tasks = requests.get('{}/todos?userId={}'.format(url, employee_id)).json()
    name_file = '{}.csv'.format(employee_id)

    with open(name_file, 'w') as f:
        for data in tasks:
            csv_write = csv.writer(f, quoting=csv.QUOTE_ALL)
            csv_write.writerow([data['userId'],
                                user_name, data['completed'], data['title']])
