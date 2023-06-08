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
    url = 'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json()['data']
        if data['dist'] == 0:
            return hot_list
        else:
            children = data['children']
            for post in children:
                hot_list.append(post['data']['title'])
            after = data['after']
            if after is None:
                return hot_list
            else:
                return recurse(subreddit, hot_list, after)
    except (KeyError, IndexError):
        return None
