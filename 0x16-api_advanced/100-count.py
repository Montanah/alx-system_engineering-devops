#!/usr/bin/python3
"""
A recursive function that queries the Reddit API, parses the
title of all hot articles, and prints a sorted count of
given keywords (case-insensitive, delimited by spaces
"""
import requests


def count_words(subreddit, word_list, after='', keywords=None):
    """
    Returns a dictionary of word counts for a given list of subreddits
    """
    url = 'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if keywords is None:
        keywords = {key: 0 for key in word_list}

    try:
        if response.json()['data']['dist'] == 0:
            return None
        for post in response.json()['data']['children']:
            title = post['data']['title'].lower()
            for word in word_list:
                keywords[word] += title.count(word)
    except (KeyError, IndexError):
        if after == '':
            return None

    if response.json()['data']['after'] is None and after == '':
        sorted_keywords = sorted(keywords.items(), key=lambda x: (-x[1], x[0]))
        for keyword, count in sorted_keywords:
            if count != 0:
                print(f"{keyword}: {count}")

    return count_words(subreddit, word_list, response.json()['data']['after'],
                       keywords)
