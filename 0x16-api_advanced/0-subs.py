#!/usr/bin/python3
"""Function to querry subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribes(subreddit):
    """Return the total numbers of subcribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'user-agent': 'request'}
    response = request.get(url, headers=headers, allow_redirrects=false)
    
    if response.status_code != 200:
        return 0
    data = response.json().get("data")
    num_subs = data.get("subscribers")

    return num_subs
