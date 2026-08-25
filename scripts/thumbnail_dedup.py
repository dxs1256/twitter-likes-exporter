#!/usr/bin/env python3
"""
Thumbnail-level dedup for twitter-likes-exporter.

Reads exports/likes_mini.json, downloads thumbnails, computes perceptual
hashes (dHash + pHash), groups visually-similar thumbnails, and writes a
detailed report alongside a links file ready for video-dedup --deep.

Entries without thumbnails are passed through untouched — they never get
filtered out, and appear in the report under a separate "no thumbnail" section.

Output (exports/):
  thumb_report.md          — full report with duplicate groups
  thumb_kept_pairs.txt     — "thumbnail_url|video_url" for unique entries
  thumb_duplicate_groups.json — machine-readable groups
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import Any

import imagehash
from PIL import Image, UnidentifiedImageError

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

INPUT_FILE: str = os.environ.get("THUMB_INPUT", "exports/likes_mini.json")
CACHE_DIR: str = os.environ.get("THUMB_CACHE", ".thumb_cache")
OUT_DIR: str = os.environ.get("THUMB_OUTDIR", "exports")

# --threshold N   Hamming-distance threshold (0-64, lower = stricter)
THRESHOLD: int = int(os.environ.get("THUMB_THRESHOLD", "10"))
# --hash-size N   hash size passed to imagehash (default 8 → 64-bit hash)
HASH_SIZE: int = int(os.environ.get("THUMB_HASH_SIZE", "8"))

# HTTP headers to avoid being blocked by CDNs
HEADERS: dict[str, str] = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/128.0.0.0 Safari/537.36"
    ),
    "Accept": "image/avif,image/webp,image/*,*/*;q=0.8",
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _cache_key(url: str) -> str:
    """Deterministic cache filename for a thumbnail URL."""
    return hashlib.sha256(url.encode()).hexdigest()[:16]


def download_thumbnail(url: str, cache_dir: Path) -> Path | None:
    """Download a thumbnail, caching to *cache_dir*.  Returns local path or None."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    dest = cache_dir / _cache_key(url)

    if dest.exists() and dest.stat().st_size > 0:
        return dest

    tmp = cache_dir / f".tmp_{_cache_key(url)}"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        if not data:
            return None
        tmp.write_bytes(data)
        tmp.rename(dest)
        return dest
    except (urllib.error.URLError, OSError) as exc:
        print(f"  [warn] download failed: {url[:80]}…  ({exc})", file=sys.stderr)
        tmp.unlink(missing_ok=True)
        return None


def compute_hashes(path: Path, hash_size: int = HASH_SIZE) -> tuple[imagehash.ImageHash, imagehash.ImageHash] | None:
    """Return (dhash, phash) for an image, or None if unreadable."""
    try:
        img = Image.open(path).convert("L")  # grayscale
    except (UnidentifiedImageError, OSError):
        return None
    return (
        imagehash.dhash(img, hash_size=hash_size),
        imagehash.phash(img, hash_size=hash_size),
    )


def hamming(a: imagehash.ImageHash, b: imagehash.ImageHash) -> int:
    """Hamming distance between two image hashes."""
    return int(a - b)  # imagehash overloads __sub__


# ---------------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------------


def load_entries(json_path: str) -> list[dict[str, Any]]:
    with open(json_path, encoding="utf-8") as f:
        return json.load(f)


def split_entries(
    entries: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Return (with_thumbnail, without_thumbnail)."""
    with_thumb: list[dict[str, Any]] = []
    without_thumb: list[dict[str, Any]] = []
    for entry in entries:
        thumb = entry.get("media_thumbnail")
        if thumb and isinstance(thumb, str) and thumb.startswith("http"):
            with_thumb.append(entry)
        else:
            without_thumb.append(entry)
    return with_thumb, without_thumb


def download_and_hash(
    entries: list[dict[str, Any]], cache_dir: Path
) -> list[dict[str, Any]]:
    """Download thumbnails and attach `_dhash`, `_phash`, `_thumb_path`."""
    results: list[dict[str, Any]] = []
    total = len(entries)
    for idx, entry in enumerate(entries, 1):
        thumb_url = entry["media_thumbnail"]
        print(f"  [{idx}/{total}] {thumb_url[:100]}…", file=sys.stderr)
        path = download_thumbnail(thumb_url, cache_dir)
        entry["_thumb_path"] = str(path) if path else None
        if path:
            hashes = compute_hashes(path)
            if hashes:
                entry["_dhash"] = str(hashes[0])
                entry["_phash"] = str(hashes[1])
            else:
                entry["_dhash"] = None
                entry["_phash"] = None
        else:
            entry["_dhash"] = None
            entry["_phash"] = None
        results.append(entry)
        time.sleep(0.1)  # be gentle
    return results


def find_groups(
    entries: list[dict[str, Any]], threshold: int = THRESHOLD
) -> list[list[dict[str, Any]]]:
    """
    Union-find grouping on dHash Hamming distance.
    Two entries are in the same group if their dHash distance ≤ *threshold*.
    """
    n = len(entries)
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    hashes: list[imagehash.ImageHash | None] = []
    for e in entries:
        h = e.get("_dhash")
        hashes.append(imagehash.hex_to_hash(h) if h else None)

    for i in range(n):
        if hashes[i] is None:
            continue
        for j in range(i + 1, n):
            if hashes[j] is None:
                continue
            d = hamming(hashes[i], hashes[j])  # type: ignore[arg-type]
            # Also cross-validate with pHash to reduce false positives
            ph_i = e_i_phash(entries, i)
            ph_j = e_i_phash(entries, j)
            if ph_i is not None and ph_j is not None:
                pd = hamming(ph_i, ph_j)
                if d <= threshold and pd <= threshold * 2:
                    union(i, j)
            elif d <= threshold:
                union(i, j)

    # Collect groups
    groups_map: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for i, entry in enumerate(entries):
        groups_map[find(i)].append(entry)

    # Filter out singletons (size 1)
    groups = [g for g in groups_map.values() if len(g) > 1]
    # Sort by size descending
    groups.sort(key=len, reverse=True)
    return groups


def e_i_phash(entries: list[dict[str, Any]], i: int) -> imagehash.ImageHash | None:
    h = entries[i].get("_phash")
    return imagehash.hex_to_hash(h) if h else None


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------


def hamming_pair(e1: dict[str, Any], e2: dict[str, Any]) -> str:
    """Human-readable distance between two entries."""
    dh1 = e1.get("_dhash")
    dh2 = e2.get("_dhash")
    ph1 = e1.get("_phash")
    ph2 = e2.get("_phash")

    parts: list[str] = []
    if dh1 and dh2:
        d = hamming(imagehash.hex_to_hash(dh1), imagehash.hex_to_hash(dh2))
        parts.append(f"dHash={d}")
    if ph1 and ph2:
        p = hamming(imagehash.hex_to_hash(ph1), imagehash.hex_to_hash(ph2))
        parts.append(f"pHash={p}")
    return ", ".join(parts) if parts else "n/a"


def generate_report(
    groups: list[list[dict[str, Any]]],
    with_thumb: list[dict[str, Any]],
    without_thumb: list[dict[str, Any]],
    total: int,
) -> str:
    """Generate a Markdown report (Chinese)."""
    lines: list[str] = []
    lines.append("# 缩略图去重报告")
    lines.append("")
    lines.append(f"**输入文件**: `{INPUT_FILE}`  ")
    lines.append(f"**总条目数**: {total}  ")
    lines.append(f"**有缩略图**: {len(with_thumb)}  ")
    lines.append(f"**无缩略图**: {len(without_thumb)}  ")
    lines.append(f"**判定阈值**: dHash ≤ {THRESHOLD}, pHash ≤ {THRESHOLD * 2}  ")
    lines.append(f"**发现重复组**: {len(groups)}  ")

    dup_count = sum(len(g) for g in groups)
    lines.append(f"**重复组内条目数**: {dup_count}  ")
    lines.append("")

    # --- Groups ---
    if groups:
        lines.append("## 重复组详情")
        lines.append("")
        for gi, group in enumerate(groups, 1):
            lines.append(f"### 第 {gi} 组（{len(group)} 条）")
            lines.append("")
            lines.append("| 序号 | 用户名 | 推文链接 | 缩略图 | 指纹 |")
            lines.append("|------|--------|----------|--------|------|")
            for i, entry in enumerate(group):
                uname = entry.get("username", "?")
                url = entry.get("url", "?")
                thumb = entry.get("media_thumbnail", "?")
                if len(thumb) > 60:
                    thumb_short = thumb[:57] + "..."
                else:
                    thumb_short = thumb
                dh = entry.get("_dhash", "?")
                ph = entry.get("_phash", "?")
                hash_str = f"d={dh[:8]}… p={ph[:8]}…" if dh and ph else "?"
                lines.append(
                    f"| {i+1} | @{uname} | {url} | {thumb_short} | {hash_str} |"
                )
            lines.append("")
            lines.append("**两两汉明距离：**")
            lines.append("")
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    dist = hamming_pair(group[i], group[j])
                    lines.append(
                        f"- {group[i]['url']} ↔ {group[j]['url']}  → {dist}"
                    )
            lines.append("")

    # --- No-thumbnail entries ---
    if without_thumb:
        lines.append("## 无缩略图条目")
        lines.append("")
        lines.append(
            "以下条目没有 `media_thumbnail` 字段，未参与缩略图比对，**不会被过滤掉**。"
        )
        lines.append("")
        lines.append("| 序号 | 用户名 | 推文链接 |")
        lines.append("|------|--------|----------|")
        for i, entry in enumerate(without_thumb, 1):
            lines.append(
                f"| {i} | @{entry.get('username', '?')} | {entry.get('url', '?')} |"
            )
        lines.append("")

    # --- Kept pairs ---
    lines.append("## 去重后保留列表")
    lines.append("")
    lines.append(
        "每个重复组保留一个代表 + 所有独立条目。  "
        "格式 `缩略图URL|视频URL`，可直接用于 `video-dedup --deep --thumbs`。"
    )
    lines.append("")

    seen_in_group: set[int] = set()
    for group in groups:
        for entry in group:
            seen_in_group.add(id(entry))

    kept_pairs: list[str] = []

    for group in groups:
        rep = group[0]
        thumb = rep.get("media_thumbnail", "")
        media = rep.get("media_url") or rep.get("url", "")
        kept_pairs.append(f"{thumb}|{media}  <!-- {len(group)}条重复 -->")

    for entry in with_thumb:
        if id(entry) not in seen_in_group:
            thumb = entry.get("media_thumbnail", "")
            media = entry.get("media_url") or entry.get("url", "")
            kept_pairs.append(f"{thumb}|{media}")

    for pair in kept_pairs:
        lines.append(f"- `{pair[:120]}{'...' if len(pair) > 120 else ''}`")

    lines.append("")
    lines.append(
        f"*报告生成时间：{time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}*"
    )

    return "\n".join(lines)


def write_outputs(
    groups: list[list[dict[str, Any]]],
    with_thumb: list[dict[str, Any]],
    without_thumb: list[dict[str, Any]],
    total: int,
    out_dir: str,
) -> None:
    """Write report.md, kept_pairs.txt, and duplicate_groups.json."""
    os.makedirs(out_dir, exist_ok=True)

    # --- Markdown report (root of repo) ---
    report = generate_report(groups, with_thumb, without_thumb, total)
    report_path = "report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"Report → {report_path}")

    # --- kept_pairs.txt ---
    seen_in_group: set[int] = set()
    for group in groups:
        for entry in group:
            seen_in_group.add(id(entry))

    kept_lines: list[str] = []
    for group in groups:
        rep = group[0]
        thumb = rep.get("media_thumbnail", "")
        media = rep.get("media_url") or rep.get("url", "")
        kept_lines.append(f"{thumb}|{media}")

    for entry in with_thumb:
        if id(entry) not in seen_in_group:
            thumb = entry.get("media_thumbnail", "")
            media = entry.get("media_url") or entry.get("url", "")
            kept_lines.append(f"{thumb}|{media}")

    # Also include entries without thumbnails
    for entry in without_thumb:
        url = entry.get("url", "")
        kept_lines.append(url)

    kept_path = os.path.join(out_dir, "thumb_kept_pairs.txt")
    with open(kept_path, "w", encoding="utf-8") as f:
        f.write("\n".join(kept_lines) + "\n")
    print(f"Kept pairs → {kept_path}  ({len(kept_lines)} entries)")

    # --- duplicate_groups.json (machine-readable) ---
    groups_json: list[dict[str, Any]] = []
    for gi, group in enumerate(groups, 1):
        entries_json: list[dict[str, Any]] = []
        for entry in group:
            entries_json.append(
                {
                    "username": entry.get("username"),
                    "display_name": entry.get("display_name"),
                    "url": entry.get("url"),
                    "media_url": entry.get("media_url"),
                    "media_thumbnail": entry.get("media_thumbnail"),
                    "text": (entry.get("text") or "")[:200],
                }
            )
        groups_json.append({"group_id": gi, "size": len(group), "entries": entries_json})

    json_path = os.path.join(out_dir, "thumb_duplicate_groups.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(groups_json, f, ensure_ascii=False, indent=2)
    print(f"Machine-readable → {json_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    print(f"=== Thumbnail Dedup ===", file=sys.stderr)
    print(f"Input:  {INPUT_FILE}", file=sys.stderr)
    print(f"Cache:  {CACHE_DIR}", file=sys.stderr)
    print(f"Output: {OUT_DIR}", file=sys.stderr)
    print(f"Threshold: dHash ≤ {THRESHOLD}, pHash ≤ {THRESHOLD * 2}", file=sys.stderr)

    # 1. Load
    entries = load_entries(INPUT_FILE)
    total = len(entries)
    print(f"\nLoaded {total} entries", file=sys.stderr)

    # 2. Split
    with_thumb, without_thumb = split_entries(entries)
    print(
        f"With thumbnail: {len(with_thumb)}  |  Without: {len(without_thumb)}",
        file=sys.stderr,
    )

    # 3. Download + hash
    if with_thumb:
        print(f"\nDownloading {len(with_thumb)} thumbnails…", file=sys.stderr)
        cache_dir = Path(CACHE_DIR)
        with_thumb = download_and_hash(with_thumb, cache_dir)
        hashed = sum(1 for e in with_thumb if e.get("_dhash"))
        print(f"Successfully hashed: {hashed}/{len(with_thumb)}", file=sys.stderr)
    else:
        print("\nNo thumbnails to process.", file=sys.stderr)

    # 4. Find groups
    groups: list[list[dict[str, Any]]] = []
    if with_thumb:
        hashable = [e for e in with_thumb if e.get("_dhash")]
        print(f"\nComparing {len(hashable)} hashable entries…", file=sys.stderr)
        groups = find_groups(hashable, THRESHOLD)
        print(f"Found {len(groups)} duplicate groups", file=sys.stderr)
        for gi, group in enumerate(groups, 1):
            urls = [e["url"] for e in group]
            print(f"  Group {gi}: {len(group)} entries", file=sys.stderr)
            for u in urls:
                print(f"    {u}", file=sys.stderr)

    # 5. Write outputs
    print(f"\nWriting outputs to {OUT_DIR}/ …", file=sys.stderr)
    write_outputs(groups, with_thumb, without_thumb, total, OUT_DIR)

    print("\nDone.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())