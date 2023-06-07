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
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        for post in response.json().get('data').get('children'):
            hot_list.append(post.get('data').get('title'))
        after = response.json().get('data').get('after')
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None