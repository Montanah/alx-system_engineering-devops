#!/usr/bin/python3
"""a script that exports data in the CSV format"""

if __name__ == "__main__":
    import requests
    from sys import argv

    employee_ID = int(argv[1])
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(employee_ID))
    employee_name = r.json().get('username')

    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = r.json()
    all_tasks = [item for item in tasks if item.get('userId') == employee_ID]

    with open('{}.csv'.format(employee_ID), 'w+') as f:
        for item in all_tasks:
            f.write('"{}","{}","{}","{}"\n'.format(employee_ID, employee_name,
                                                   item.get('completed'),
                                                   item.get('title')))
f.closed
