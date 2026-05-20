#!/usr/bin/env python3
"""Configure tweetxvault auth from environment variables."""

import os
from pathlib import Path


def main():
    auth_token = os.environ["AUTH_TOKEN"]
    ct0 = os.environ["CT0"]
    user_id = os.environ["USER_ID"]

    config_dir = Path.home() / ".config" / "tweetxvault"
    config_dir.mkdir(parents=True, exist_ok=True)

    config_file = config_dir / "config.toml"
    config_file.write_text(
        f'[auth]\n'
        f'auth_token = "{auth_token}"\n'
        f'ct0 = "{ct0}"\n'
        f'user_id = "{user_id}"\n'
    )
    print(f"Auth configured at {config_file}")


if __name__ == "__main__":
    main()
