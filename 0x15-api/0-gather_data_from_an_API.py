#!/usr/bin/python3
'''A script that returns information about an employee's TODO list progress'''

if __name__ == "__main__":
	import requests
	from sys import argv

	employee_ID = int(argv[1])
	r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(employee_ID))
	employee_name = r.json().get('name')

	r = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = r.json()
    all_tasks = [item for item in tasks if item.get('userId') == employee_ID]
    done_tasks = [item for item in all_tasks if item.get('completed') is True]

    print('Employee {} is done with tasks({}/{}):'.format(employee_name,
                                                          len(done_tasks),
                                                          len(all_tasks)))
    for task in done_tasks:
        print('\t {}'.format(task.get('title')))
