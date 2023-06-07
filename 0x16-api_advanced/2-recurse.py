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
        data = response.json().get('data')
        if data and data.get('children'):
            children = data.get('children')
            for post in children:
                title = post.get('data').get('title')
                hot_list.append(title)

            """Check if there are more pages"""
            after = data.get('after')
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return hot_list
    else:
        return None