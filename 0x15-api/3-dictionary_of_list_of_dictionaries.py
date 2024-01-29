#!/usr/bin/python3
"""extended Python script to export data in JSON format"""
import json
import requests
from sys import argv


def gatherdata(employeeID):
    """Gather data from an API and export it to JSON"""
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employeeID}/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{employeeID}"

    try:
        response = requests.get(user_url)
        if response.status_code == 200:
            users = response.json()
            response = requests.get(todo_url)
            if response.status_code == 200:
                todos = response.json()
                with open('todo_all_employees.json', 'w') as jsonfile:
                    json.dump({user['id']: [{
                        "task": todo['title'],
                        "completed": todo['completed'],
                        "username": user['username']
                    } for todo in todos if todo['userId'] == user['id']]
                      for user in users}, jsonfile)
            else:
                print("An error occured")
        else:
            print("An error occured")
    except (Exception):
        print("An error occured")
        return 0


if __name__ == "__main__":
    """ Only executes as main"""
    gatherdata()
