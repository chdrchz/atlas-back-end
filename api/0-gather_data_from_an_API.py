#!/usr/bin/python3
"""This module defines a script that connects to an API"""
import requests


def display_employee_progress(employee_id):
    """ script must display to stdout the employee todo list progress """
    site_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{site_url}/users/{employee_id}"
    todo_url = f"{site_url}/todos"

    employee_data = requests.get(employee_url).json()
    todo_data = requests.get(todo_url,
                             params={"userId": employee_id}).json()

    empl_name = employee_data.get("name")
    completed_tasks = [t["title"] for t in todo_data if t["completed"]]
    tasks_done = len(completed_tasks)
    tasks_total = len(todo_data)

    print("Employee {} is done with tasks({}/{}):"
          .format(empl_name, tasks_done, tasks_total))
    for task in completed_tasks:
        print(f"\t {task}")
    
if __name__ == "__main__":
    import sys

    display_employee_progress(int(sys.argv[1]))
