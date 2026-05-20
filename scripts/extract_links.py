#!/usr/bin/env python3
"""Extract tweet links from tweetxvault JSON export."""

import json
import sys
from pathlib import Path


def extract_links(json_path: str) -> list[str]:
    """Read JSON export and return list of tweet URLs."""
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    
    links = []
    for tweet in data:
        username = tweet.get("author_username")
        tweet_id = tweet.get("tweet_id")
        if username and tweet_id:
            links.append(f"https://x.com/{username}/status/{tweet_id}")
    
    return links


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <json_path>", file=sys.stderr)
        sys.exit(1)
    
    json_path = sys.argv[1]
    links = extract_links(json_path)
    
    for link in links:
        print(link)
