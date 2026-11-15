#!/usr/bin/python3
"""
Script that exports employee TODO list data to a JSON file.
"""

import json
import requests
import sys


def export_to_json(employee_id):
    """Export all tasks for a given employee ID to a JSON file."""

    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    )
    user_data = requests.get(user_url).json()

    if not user_data:
        print("Employee not found.")
        return

    username = user_data.get("username")

    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id
        )
    )
    todos = requests.get(todos_url).json()

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    filename = "{}.json".format(employee_id)

    with open(filename, "w") as jsonfile:
        json.dump({str(employee_id): tasks}, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)
    try:
        emp_id = int(sys.argv[1])
        export_to_json(emp_id)
    except ValueError:
        print("Employee ID must be an integer.")
