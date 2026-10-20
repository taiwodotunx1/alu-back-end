#!/usr/bin/python3
"""Script that returns information about an employee's TODO list progress."""
import requests
import sys

employee_id = int(sys.argv[1])

user = requests.get(
    f"https://jsonplaceholder.typicode.com/users/{employee_id}"
).json()
name = user["name"]

todos = requests.get(
    f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
).json()

total = len(todos)
done_tasks = [task for task in todos if task["completed"]]
done_count = len(done_tasks)

print(f"Employee {name} is done with tasks({done_count}/{total}):")
for task in done_tasks:
    print(f"\t {task['title']}")
