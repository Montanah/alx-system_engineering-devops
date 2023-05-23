#!/usr/bin/python3
''' a script to save task information in JSON format '''

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    employee_ID = argv[1]
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(employee_ID))
    employee_name = r.json().get('username')

    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = r.json()
    all_tasks = [item for item in tasks if item.get('userId') ==
                 int(employee_ID)]

    emp_dict = {employee_ID: []}
    for task in all_tasks:
        emp_dict.get(employee_ID).append({'task': task.get('title'),
                                          'completed': task.get('completed'),
                                          'username': employee_name})

    with open('{}.json'.format(employee_ID), 'w+') as f:
        json.dump(emp_dict, f)
    f.closed
