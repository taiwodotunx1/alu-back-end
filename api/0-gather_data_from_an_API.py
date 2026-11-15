#!/usr/bin/python3
"""Gather employee TODO list progress from an API."""

import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    employee = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    ).json()

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id
        )
    ).json()

    completed_tasks = [
        task for task in todos if task.get("completed") is True
    ]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee["name"], len(completed_tasks), len(todos)
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task["title"]))
