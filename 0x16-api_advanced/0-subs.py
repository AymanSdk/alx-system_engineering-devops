#!/usr/bin/python3
"""get number of subscribers for a given subreddit"""
from requests import get
from sys import argv


def number_of_subscribers(subreddit):
    """get number of subscribers for a given subreddit"""
    head = {'User-Agent': 'Aymane sadiki'}
    count = get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), headers=head).json()
    try:
        return count.get('data').get('subscribers')
    except AttributeError:
        return 0


if __name__ == '__main__':
    number_of_subscribers(argv[1])
