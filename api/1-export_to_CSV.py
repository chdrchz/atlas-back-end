#!/usr/bin/python3
"""This module defines a script that connects to an API"""
import csv
import os
import requests
import sys


def employee_todo_list(employee_id):
    """This function exports to a csv"""

    # API URLs
    site_url = "https://jsonplaceholder.typicode.com/"
    employee_url = f"{site_url}/users/{employee_id}"
    todo_url = f"{site_url}/todos"

    # get employee data
    employee_data = requests.get(employee_url).json()
    employee_name = employee_data['name']
    todo_list = requests.get(todo_url, params={"userId": employee_id}).json()

    # employees tasks
    todo_list = requests.get(todo_url, params={"userId": employee_id}).json()

    # prepare CSV data
    csv_data = [["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]]
    for todo in todo_list:
        if todo["completed"]:
            task_completed_status = "Completed"
        else:
            task_completed_status = "Not Completed"
        csv_row = [
            employee_id,
            employee_name,
            task_completed_status,
            todo["title"]
        ]
        csv_data.append(csv_row)

    # export to CSV
    csv_file_path = f"{employee_id}.csv"
    if os.path.exists(csv_file_path):
        print(f"File '{csv_file_path}' already exists. Not overwriting.")
    else:
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(csv_data)
        num_tasks = len(csv_data) - 1
        print(f"CSV file '{csv_file_path}' has been created with {num_tasks} tasks.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_todo_list(employee_id)
