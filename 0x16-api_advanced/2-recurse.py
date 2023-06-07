#!/usr/bin/python3
'''
A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
'''

import requests


def recurse(subreddit, hot_list=[], after=''):
    '''
    returns full list of hot posts in a subreddit
    '''
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, after)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        if response.json()['data']['dist'] == 0:
            return None
        for post in response.json()['data']['children']:
            hot_list.append(post['data']['title'])
    except (KeyError, IndexError):
        if (after == ''):
            return None

    if (response.json()['data']['after'] is None):
        return hot_list

    return recurse(subreddit, hot_list, response.json()['data']['after'])