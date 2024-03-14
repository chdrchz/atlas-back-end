#!/usr/bin/python3
"""This module defines a script that connects to an API"""
import requests
import sys


def employee_todo_list(employee_id):
    """This function displays todo list progress"""

    site_url = "https://jsonplaceholder.typicode.com/"
    employee_url = f"{site_url}/users/{employee_id}"
    todo_url = f"{site_url}/todos"

    employee_data = requests.get(employee_url).json()
    employee_name = employee_data['name']
    todo_list = requests.get(todo_url, params={"userId": employee_id}).json()

    completed_todos = [t["title"] for t in todo_list if t["completed"]]
    total_todos = len(todo_list)
    total_done = len(completed_todos)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, total_done, total_todos))

    for todo in completed_todos:
        print(f"\t {todo}")


if __name__ == "__main__":

    employee_todo_list(int(sys.argv[1]))
