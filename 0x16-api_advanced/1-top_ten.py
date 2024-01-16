#!/usr/bin/python3
"""

Function queries Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.

"""


import requests
import sys


def top_ten(subreddit):
    """ first ten hot posts """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limits': 10}
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(None)
        return
    jdict = response.json()
    hotposts = jdict['data']['children']
    if len(hotposts) == 0:
        print(None)
    else:
        for post in hotposts:
           print(post['data']['title'])
