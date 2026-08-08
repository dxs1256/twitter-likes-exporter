#!/usr/bin/env python3
"""Prune like records that were not refreshed during the latest full sync.

tweetxvault's archive is append-only: tweets you have unliked stay in storage
forever, so exports keep containing them. After a `tweetxvault sync likes
--full` run, every tweet still liked has its collection.synced_at bumped to
the current run, while unliked tweets keep their old synced_at. This script
drops records whose synced_at is older than the given sync start timestamp.
"""

import json
import sys
from datetime import datetime


def parse_timestamp(value: str) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def prune_unliked(json_path: str, sync_start: str) -> int:
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    start = parse_timestamp(sync_start)
    if start is None:
        raise ValueError(f"Invalid sync start timestamp: {sync_start!r}")

    kept = []
    removed = 0
    for tweet in data:
        collection = tweet.get("collection") or {}
        if collection.get("type") == "like":
            synced_at = parse_timestamp(collection.get("synced_at"))
            if synced_at is None or synced_at < start:
                removed += 1
                continue
        kept.append(tweet)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(kept, f, ensure_ascii=False, indent=2)

    return removed


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input.json> <sync_start_timestamp>", file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]
    sync_start = sys.argv[2]

    removed = prune_unliked(input_path, sync_start)
    print(f"清理完成: 移除 {removed} 条已取消点赞 -> {input_path}")
