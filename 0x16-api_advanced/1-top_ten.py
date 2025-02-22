#!/usr/bin/python3
"""
Hot posts
"""


def top_ten(subreddit):
    """ get hot posts """
    import requests

    try:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            for post in response.json()['data']['children']:
                print(post['data']['title'])
        else:
            print(None)

    except Exception as e:
        print(e)
