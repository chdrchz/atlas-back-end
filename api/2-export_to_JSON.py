#!/usr/bin/python3
"""This module defines a script that connects to an API"""
import json
import requests
import sys


def employee_todo_list(employee_id):
    """This function exports todo list data to json"""

    site_url = "https://jsonplaceholder.typicode.com/"
    employee_url = f"{site_url}/users/{employee_id}"
    todo_url = f"{site_url}/todos"

    employee_data = requests.get(employee_url).json()
    employee_name = employee_data['name']
    todo_list = requests.get(todo_url, params={"userId": employee_id}).json()

    completed_todos = [t["title"] for t in todo_list if t["completed"]]

    employee_json = {
        "employee_id": employee_id,
        "employee_name": employee_name,
        "tasks": todo_list
    }

    json_file_path = f"{employee_id}.json"
    with open(json_file_path, 'w') as json_file:
        json.dump(employee_json, json_file, indent=4)


if __name__ == "__main__":

    employee_todo_list(int(sys.argv[1]))
