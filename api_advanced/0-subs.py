#!/usr/bin/python3
<<<<<<< HEAD
"""DOC"""
=======
"""Return number of subscribers for a given subreddit"""
>>>>>>> 392a0234b0d8a1a499f86f9d724ff448dab57edb
import requests


def number_of_subscribers(subreddit):
<<<<<<< HEAD
    """DOC"""
    reddit_url = "https://www.reddit.com/r/{}/about.json" \
        .format(subreddit)

    header = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(reddit_url,
                            headers=header
                            )

    if response.status_code == 200:
        data = response.json()['data']
        subs = data['subscribers']
        return subs
=======
    """Return the number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json" \
        .format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data') \
            .get('subscribers')
>>>>>>> 392a0234b0d8a1a499f86f9d724ff448dab57edb
    return 0