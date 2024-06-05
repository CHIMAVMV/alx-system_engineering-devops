#!/bin/usr/
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests
import sys

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; MyRedditBot/1.0)"
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            # Subreddit not found
            print(None)
        else:
            # Other HTTP error
            print(f"HTTP error occurred: {http_err}")
            print(None)
    except requests.exceptions.RequestException as err:
        # Other request errors
        print(f"Error occurred: {err}")
        print(None)
    except KeyError:
        # In case the JSON structure is not as expected
        print(None)

# Example usage
subreddit = "python"
top_ten(subreddit)

