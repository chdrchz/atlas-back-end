#!/usr/bin/python3
"""This module defines a script that connects to an API"""
import json
import requests
import sys


def employee_todo_list(employee_id):
    """This function exports todo list data to json"""

    site_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{site_url}/users/{employee_id}"
    todo_url = f"{site_url}/todos"

    employee_data = requests.get(employee_url).json()
    employee_name = employee_data['name']
    todo_list = requests.get(todo_url, params={"userId": employee_id}).json()

    tasks = []
    for todo in todo_list:
        task = {
            "task_id": todo["id"],
            "title": todo["title"],
            "completed": todo["completed"]
        }
        tasks.append(task)

    file_path = f"{employee_id}.json"
    with open(file_path, 'w') as file:
        json.dumps(tasks, file, indent=4)
        print(f"Data for employee_id {employee_id} witten to {file_path}.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_todo_list(int(sys.argv[1]))
