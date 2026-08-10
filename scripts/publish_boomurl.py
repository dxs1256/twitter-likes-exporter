#!/usr/bin/env python3
"""Publish exports/likes_mini.json to boomurl xlikes site.

Reads the boomurl API key from the BOOMURL_KEY environment variable.
The API key can be a bearer token (starts with "boom_") or a raw API key.
"""

import base64
import json
import os
import sys
import urllib.request

SITE = "xlikes"
API_URL = f"https://boomurl.com/api/v1/sites/{SITE}"


def main() -> int:
    key = os.environ.get("BOOMURL_KEY", "")
    if not key:
        print("ERROR: BOOMURL_KEY environment variable is not set", file=sys.stderr)
        return 1

    with open("exports/likes_mini.json", "rb") as f:
        raw = f.read()

    payload = {
        "base64": True,
        "files": {
            "index.json": base64.b64encode(raw).decode(),
        },
    }

    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode(),
        method="PUT",
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = resp.read().decode()
            print(f"boomurl response: {body}")
            try:
                parsed = json.loads(body)
                if parsed.get("ok") is True:
                    return 0
            except json.JSONDecodeError:
                pass
            print("boomurl publish failed", file=sys.stderr)
            return 1
    except urllib.error.HTTPError as e:
        print(f"boomurl HTTP error: {e.code} {e.reason}", file=sys.stderr)
        print(e.read().decode(), file=sys.stderr)
        return 1
    except urllib.error.URLError as e:
        print(f"boomurl connection error: {e.reason}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
