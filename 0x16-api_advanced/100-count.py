#!/usr/bin/python3
"""
Advanced API calling
3. Count it!
"""


def count_words(subreddit, word_list, params='', all_words=[]):
    """match given word phrases present in the api"""
    from collections import Counter
    import json
    import requests
    import sys

    try:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code == 200:
            for post in response.json()['data']['children']:
                count = 0
                all_words.extend(
                    [word for word in post['data']['title'].split(" ") if word in word_list ]
                )


            params = {'after': response.json()['data']['after']}

            if response.json()['data']['after']:
                return count_words(subreddit, word_list, params, all_words)

            counter = Counter(all_words)
            for word in counter:
                sys.stdout.write(f"{word}: {counter[word]}\n")
        else:
            return None

    except Exception as e:
        print(e)

