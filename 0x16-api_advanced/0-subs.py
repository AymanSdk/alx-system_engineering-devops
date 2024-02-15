#!/usr/bin/python3
""" Get how many subscribers """
import requests


def number_of_subscribers(subreddit):
    """ get how many subscribers """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers={})

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
