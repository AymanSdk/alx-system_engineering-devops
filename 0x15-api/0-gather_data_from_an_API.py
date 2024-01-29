#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    to_do = requests.get(url + "todos?userId={}".format(sys.argv[1])).json()
    
    
    completed_tasks = [t.get("title") for t in to_do if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"), len(completed_tasks), len(to_do)))
    [print("\t {}".format(task)) for task in completed_tasks]
