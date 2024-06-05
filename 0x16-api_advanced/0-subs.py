#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests
import sys

def get_subreddit_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; MyRedditBot/1.0)"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["data"]["subscribers"]
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            # Subreddit not found
            return 0
        else:
            # Other HTTP error
            print(f"HTTP error occurred: {http_err}")
            return 0
    except requests.exceptions.RequestException as err:
        # Other request errors
        print(f"Error occurred: {err}")
        return 0
    except KeyError:
        # In case the JSON structure is not as expected
        return 0

# Example usage
subreddit = "python"
subscribers = get_subreddit_subscribers(subreddit)
print(f"Subscribers for subreddit '{subreddit}': {subscribers}")

