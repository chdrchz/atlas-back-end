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

    completed_todos = [t["title"] for t in todo_list if t["completed"]]
    total_todos = len(todo_list)
    total_done = len(completed_todos)

    task_progress = f"{total_done}/{total_todos}"
    print(f"Employee {employee_name} is done with tasks({task_progress}):")
