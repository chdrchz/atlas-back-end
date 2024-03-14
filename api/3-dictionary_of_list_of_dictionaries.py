#!/usr/bin/python3
"""This module defines a script that connects to an API"""
import json
import requests
import sys


def employee_todo_list():
    """Records all tasks from all employees"""

    site_url = "https://jsonplaceholder.typicode.com"
    all_employees_tasks = {}
    employee_id = 1

    while True:
        employee_url = f"{site_url}/users/{employee_id}"
        response = requests.get(employee_url)

        if response.status_code != 200:
            break

        employee_data = response.json()
        username = employee_data.get('username')

        todo_url = f"{site_url}/todos"
        todo_list = requests.get(todo_url, params={"userId": employee_id}).json()

        all_employees_tasks[str(employee_id)] = [{"username": username,
                                                   "task": todo['title'],
                                                   "completed": todo['completed']} 
                                                   for todo in todo_list]

        employee_id += 1

    with open("todo_all_employees.json", 'w') as f:
        json.dump(all_employees_tasks, f, indent=4)


if __name__ == "__main__":

    employee_todo_list(int(sys.argv[1]))
