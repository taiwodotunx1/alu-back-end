#!/usr/bin/python3
"""
Script that exports employee TODO list data to a CSV file.
"""

import csv
import requests
import sys


def export_to_csv(employee_id):
    """Export all tasks for a given employee ID to a CSV file."""

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

    filename = "{}.csv".format(employee_id)

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    try:
        emp_id = int(sys.argv[1])
        export_to_csv(emp_id)
    except ValueError:
        print("Employee ID must be an integer.")
