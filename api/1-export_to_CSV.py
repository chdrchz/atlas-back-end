#!/usr/bin/python3
"""This module defines a script that connects to an API"""
import csv
import os
import requests


def employee_todo_list(employee_id):
    """This function exports to a csv"""

    site_url = "https://jsonplaceholder.typicode.com/"
    employee_url = f"{site_url}/users/{employee_id}"
    todo_url = f"{site_url}/todos"

    employee_data = requests.get(employee_url).json()
    employee_name = employee_data['name']
    todo_list = requests.get(todo_url, params={"userId": employee_id}).json()

    completed_todos = [t["title"] for t in todo_list if t["completed"]]
    total_todos = len(todo_list)
    total_done = len(completed_todos)

    csv_data = [["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]]
    for todo in todo_list:
        csv_row = [employee_id, employee_name, completed_todos, todo["title"]]
        csv_data.append(csv_row)
    # export to csv
    csv_file_path = f"{employee_id}.csv"
    if os.path.exists(csv_file_path):
        print(f"File '{csv_file_path}' already exists. Not overwriting.")
    else:
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(csv_data)


if __name__ == "__main__":
    import sys

    employee_id = int(sys.argv[1])
    employee_todo_list(employee_id)
