#!/usr/bin/python3
"""
Hot posts recursive
"""


def recurse(subreddit, params='', hot_list=[]):
    """ get hot posts """
    import json
    import requests

    try:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(
            url, headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code == 200:

            for post in response.json()['data']['children']:
                hot_list.append(post['data']['title'])

            params = {'after': response.json()['data']['after']}

            if response.json()['data']['after']:
                return recurse(subreddit, params, hot_list)

            return hot_list
        else:
            return None

    except Exception as e:
        print(e)
