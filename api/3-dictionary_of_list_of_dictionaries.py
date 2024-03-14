#!/usr/bin/python3
"""This module defines a script that connects to an API"""
import json
import requests


def all_employee_todo_lists(employee_id):
    """This function exports todo list data to json"""

    site_url = "https://jsonplaceholder.typicode.com"
    employees_url = f"{site_url}/users/"
    todos_url = f"{site_url}/todos"
    
    employees = requests.get(employees_url).json()

    for employee in employees:
        employee_id = employee['id']
        username = employee['username']

    todo_list = requests.get(todos_url, params={"userId": employee_id}).json()

    data = [{
        "task": todo['title'],
        "completed": todo['completed'],
        "username": username
    } for todo in todo_list]

    format = {str(employee_id): data}

    file = f"{employee_id}.json"
    with open(file, 'w') as f:
        json.dump(format, f)


if __name__ == "__main__":
    all_employee_todo_lists()
