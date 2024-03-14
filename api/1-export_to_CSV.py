#!/usr/bin/python3
""" This module defines a function that exports to a csv """
import csv
import requests
import sys


def employee_todo_list(employee_id):
    """This function exports todo list tasks to a csv"""

    site_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{site_url}/users/{employee_id}"
    todo_url = f"{site_url}/todos"

    employee_data = requests.get(employee_url).json()
    username = employee_data.get('username')

    todos = requests.get(todo_url, params={'userId': employee_id}).json()
    csv_file_name = f"{employee_id}.csv"
    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([employee_id, username,
                             todo['completed'], todo['title']])


if __name__ == "__main__":

    employee_todo_list(int(sys.argv[1]))
