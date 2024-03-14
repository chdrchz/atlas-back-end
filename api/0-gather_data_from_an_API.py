#!/usr/bin/python3
"""This module defines a script that connects to an API"""
import requests


def employee_todo_list(employee_id):
    """This function displays todo list progress"""

    site_url = "https://jsonplaceholder.typicode.com/"
    employee_url = f"{site_url}/users/{employee_id}"
    todo_url = f"{site_url}/todos"

    employee_name = requests.get(employee_url).json()
    todo_list = requests.get(todo_url, params={"userId": employee_id}).json()

    completed_todos = [todo["title"] for todo in todo_list if todo["completed"]]
    total_todos = len(todo_list)
    total_done = len(completed_todos)

    print("Employee {} is done with tasks({}/{}):".format(employee_name, total_done, total_todos))
