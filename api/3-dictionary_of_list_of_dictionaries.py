#!/usr/bin/python3
"""
Script that exports all employees TODO list data to a JSON file.
"""

import json
import requests


def export_all_to_json():
    """Export all tasks for all employees to a JSON file."""

    users_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(users_url).json()

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos = requests.get(todos_url).json()

    all_tasks = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")

        user_tasks = []
        for task in todos:
            if task.get("userId") == user.get("id"):
                user_tasks.append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

        all_tasks[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)


if __name__ == "__main__":
    export_all_to_json()
