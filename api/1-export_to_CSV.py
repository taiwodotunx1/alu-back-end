#!/usr/bin/python3
"""
Fetch an employee's TODO list from the JSONPlaceholder REST API
and export all of their tasks to a CSV file named USER_ID.csv.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    employee_id = int(sys.argv[1])

    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get("{}/todos".format(base_url),
                         params={"userId": employee_id}).json()

    username = user.get("username")

    with open("{}.csv".format(employee_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL,
                            lineterminator="\n")
        for task in todos:
            writer.writerow([employee_id, username,
                             task.get("completed"), task.get("title")])
