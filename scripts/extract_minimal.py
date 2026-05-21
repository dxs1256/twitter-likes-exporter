#!/usr/bin/env python3
"""Extract minimal tweet info from tweetxvault JSON export."""

import json
import sys


def get_best_media_url(media_item: dict) -> str | None:
    """Get the highest bitrate video URL or direct image URL."""
    variants = media_item.get("variants", [])
    if variants:
        best = max(variants, key=lambda v: v.get("bitrate") or 0)
        return best.get("url")
    return media_item.get("url")


def extract_minimal(json_path: str) -> list[dict]:
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
    
    result = []
    for tweet in data:
        author = tweet.get("author") or {}
        
        media_urls = []
        for m in tweet.get("media", []):
            url = get_best_media_url(m)
            if url:
                media_urls.append(url)
        
        entry = {
            "tweet_id": tweet.get("tweet_id"),
            "text": tweet.get("text"),
            "username": author.get("username"),
            "display_name": author.get("display_name"),
            "created_at": tweet.get("created_at"),
            "media_url": media_urls[0] if media_urls else None,
        }
        result.append(entry)
    
    return result


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <input.json> <output.json>", file=sys.stderr)
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    minimal_data = extract_minimal(input_path)
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(minimal_data, f, ensure_ascii=False, indent=2)
    
    print(f"精简完成: {len(minimal_data)} 条 -> {output_path}")
