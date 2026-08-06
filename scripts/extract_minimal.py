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


def get_media_thumbnail(media_item: dict) -> str | None:
    """Get the video cover / thumbnail URL."""
    # tweetxvault export stores thumbnail in "thumbnail_url"
    return media_item.get("thumbnail_url")


def get_card_video_media(tweet: dict) -> list[dict]:
    """Extract videos embedded in unified_card (amplify/ad cards).

    Some tweets (e.g. promoted "video_website" cards) only carry their video
    inside raw_json.card.binding_values instead of the usual entities.media,
    so tweetxvault never exposes it in the normalized "media" field.
    """
    raw = tweet.get("raw_json") or {}
    card = raw.get("card") or {}
    legacy = card.get("legacy") or {}

    result = []
    for binding in legacy.get("binding_values") or []:
        value = binding.get("value") or {}
        raw_card = value.get("string_value")
        if not isinstance(raw_card, str) or "media_entities" not in raw_card:
            continue
        try:
            parsed = json.loads(raw_card)
        except (ValueError, TypeError):
            continue

        for entity in (parsed.get("media_entities") or {}).values():
            if not isinstance(entity, dict) or entity.get("type") != "video":
                continue
            variants = []
            for variant in (entity.get("video_info") or {}).get("variants") or []:
                if isinstance(variant, dict) and variant.get("url"):
                    variants.append(
                        {
                            "bitrate": variant.get("bitrate"),
                            "content_type": variant.get("content_type"),
                            "url": variant.get("url"),
                        }
                    )
            if not variants:
                continue
            thumb = entity.get("media_url_https") or entity.get("media_url")
            result.append(
                {
                    "type": "video",
                    "url": thumb,
                    "thumbnail_url": thumb,
                    "variants": variants,
                }
            )
    return result


def extract_minimal(json_path: str) -> list[dict]:
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    result = []
    for tweet in data:
        author = tweet.get("author") or {}

        tweet_id = tweet.get("tweet_id")
        username = author.get("username")
        url = f"https://x.com/{username}/status/{tweet_id}" if username and tweet_id else None

        media_items = list(tweet.get("media", []))
        media_items.extend(get_card_video_media(tweet))

        media_urls = []
        media_thumbnails = []
        for m in media_items:
            m_url = get_best_media_url(m)
            if m_url:
                media_urls.append(m_url)
            thumb = get_media_thumbnail(m)
            if thumb:
                media_thumbnails.append(thumb)

        entry = {
            "username": username,
            "display_name": author.get("display_name"),
            "created_at": tweet.get("created_at"),
            "url": url,
            "media_url": media_urls[0] if media_urls else None,
            "media_thumbnail": media_thumbnails[0] if media_thumbnails else None,
            "text": tweet.get("text"),
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