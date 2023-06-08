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

    if response.status_code != 200:
        return

    try:
        data = response.json()['data']
        if data['dist'] == 0:
            sorted_keywords = sorted(keywords.items(),
                                     key=lambda x: (-x[1], x[0]))
            for keyword, count in sorted_keywords:
                print(f'{keyword}: {count}')
            return
        else:
            children = data['children']
            for post in children:
                title = post['data']['title']
                words = title.lower().split()
                for word in words:
                    # Ignore variations of word endings
                    if word.endswith(('.', '!', '_')):
                        continue
                    # Convert Javascript to javascript for counting
                    if word == 'javascript':
                        word = 'java'
                    if word in word_list:
                        keywords[word] = keywords.get(word, 0) + 1

            after = data['after']
            return count_words(subreddit, word_list, after, keywords)
    except (KeyError, IndexError):
        return
