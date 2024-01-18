#!/usr/bin/python3
"""

Function queries the Reddit API and returns the number of subscribers

"""


import requests


def number_of_subscribers(subreddit):
    """ queries reddit api """
    headers = {'User-Agent': 'firstscript/1.0 by Exciting-Professor45'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0
    jdict = response.json()
    if 'data' not in jdict:
        return 0
    if 'subscribers' not in jdict.get('data'):
        return 0
    return response.json()['data']['subscribers']
