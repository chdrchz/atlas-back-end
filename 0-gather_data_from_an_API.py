#!/usr/bin/python3
"""This module defines a script that connects to an API"""
import requests


def employee_todo_list(employee_id):
    """This function displays todo list progress"""
    url = "https://jsonplaceholder.typicode.com/"
    employee_url = f"{url}/users/{employee_id}"
    todo_url = f"{url}/todos"

    employee_name = requests.get(employee_url).json()
    todo_list = requests.get(todo_url, params={"userId": employee_id}).json()
