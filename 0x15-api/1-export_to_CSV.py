#!/usr/bin/python3
"""Export to CSV"""
import requests
import csv
from sys import argv


def gatherdata(employeeID):
    """prints data from api"""
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employeeID}/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{employeeID}"

    try:
        response = requests.get(user_url)
        if response.status_code == 200:
            user = response.json()
            response = requests.get(todo_url)
            if response.status_code == 200:
                todos = response.json()
                with open('{}.csv'.format(employeeID), 'w') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',',
                                        quotechar='"', quoting=csv.QUOTE_ALL)
                    for todo in todos:
                        writer.writerow([todo['userId'], user['username'],
                                        todo['completed'], todo['title']])
            else:
                print("An error occured")
        else:
            print("An error occured")
    except (Exception):
        print("An error occured")
        return 0


if __name__ == "__main__":
    """ Only executes as main"""
    if len(argv) == 2 and argv[1].isdigit():
        gatherdata(argv[1])
    else:
        print("Usage: ./1-export_to_CSV.py <employee ID>")
