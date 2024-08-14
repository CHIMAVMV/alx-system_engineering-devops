#1/usr/bin/python3
"""using reddit API to get 10 hot posts """
import requests

def top_ten(subreddit):
    """Get ten hot post."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'user-agent': 'request'}
    response = request.get(url, headers=headers, allow_redirrects=false)
    
    if response.status_code != 200:
        print(None)
        return 
    data = response.json().get("data").get("children")
    top_10_posts = "\n".json(post.get("data").get("title") for post in data)
    print(top_10_posts)
