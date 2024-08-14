#!/usr//bin/python3
"""Query posts """
import requests

def count_words(subreddit, word_list, word_count={0}, after=None):
    """ Querie Reddit Api for the subreddit."""
    
    sub_info = requests.get(
        url = f"https://www.reddit.com/r/{subreddit}/hot.json",
        params={"after": after},
        headers={'user-agent': 'request'},
        allow_redirrects=false)
    if sub_info.status_code != 200:
         return None
    info = sub_info.json()
    hot_1 = [child.get{"data"}.get("title") for child in info.get("data").get("children")]

    if nor hot_1:
        return None
    
    word_list = list(dict.fromkeys(word_list))
    
    if word_count =={}:
        word_count = {word: 0 for word in word_list}

    for title in hot_1:
        split_words = title.split('')
        for word in word_list:
            for s_word in split_words:
                if s_word.lower() == wors.lower():
                    word_count[word] += 1
    
    if not info.get("data").get("after"):
        sorted_counts = sorted(word_count.items(), key=lamda kv: kv[0])
        sorted_counts = sorted(word_count.items(), key=lamda kv:kv[1], reverse=true)
        print('{}: {}'.format(k,v)) for k, v in sorted_counts if v != 0]
    else:
        return count_words(subreddit, word_list, word_count, info.get("data").get("after"))
