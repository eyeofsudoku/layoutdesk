#!/usr/bin/env python3
"""
Publish the work journal to Bear.

  python publish.py posts   -> create or update every post in posts/*.md
  python publish.py blog    -> apply blog.json (title, home page, navigation)
  add --dry-run to print what would be sent

Each post is a Markdown file with a small header:

    ---
    title: The title
    slug: the-address
    date: 2026-11-19T10:00:00+01:00
    tags: [pdf-accessibility, indesign]
    meta_description: One or two sentences for search results.
    ---
    The article in Markdown.

Posts already on Bear are remembered in posts/published.json (slug -> uid),
so editing a file and running again updates the post instead of duplicating it.
Needs BEAR_API_KEY and BEAR_SUBDOMAIN. Standard library only.
"""

import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
POSTS = HERE / "posts"
STATE = POSTS / "published.json"
USER_AGENT = "dtp-journal/1.0 (+https://github.com/eyeofsudoku)"


class Bear:
    def __init__(self, subdomain, key, dry_run=False):
        self.root = f"https://bearblog.dev/{subdomain}/api/v1/"
        self.key = key
        self.dry_run = dry_run

    def call(self, method, path, body=None):
        if self.dry_run and method != "GET":
            print(f"  [dry run] {method} {path} {json.dumps(body, ensure_ascii=False)[:160]}")
            return {"uid": "DRYRUN", "url": "(dry run)"}
        data = json.dumps(body).encode() if body is not None else None
        for attempt in range(4):
            req = urllib.request.Request(self.root + path, data=data, method=method)
            req.add_header("Authorization", f"Bearer {self.key}")
            req.add_header("Accept", "application/json")
            req.add_header("User-Agent", USER_AGENT)
            if data is not None:
                req.add_header("Content-Type", "application/json")
            try:
                with urllib.request.urlopen(req, timeout=30) as r:
                    raw = r.read()
                    return json.loads(raw) if raw else {}
            except urllib.error.HTTPError as e:
                if e.code == 429 and attempt < 3:
                    time.sleep(int(e.headers.get("Retry-After", "10")) + 1)
                    continue
                if e.code >= 500 and attempt < 3:
                    time.sleep(10)
                    continue
                msg = e.read().decode(errors="replace")[:300]
                raise SystemExit(f"Bear API {method} {path} -> {e.code}: {msg}")
            except (urllib.error.URLError, TimeoutError) as e:
                if attempt < 3:
                    time.sleep(10)
                    continue
                raise SystemExit(f"Bear API {method} {path} unreachable: {e}")


def parse(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise SystemExit(f"{path.name}: missing the --- header")
    meta = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            v = [t.strip() for t in v[1:-1].split(",") if t.strip()]
        meta[k.strip()] = v
    for need in ("title", "slug", "date"):
        if not meta.get(need):
            raise SystemExit(f"{path.name}: '{need}' is missing in the header")
    return meta, m.group(2).strip() + "\n"


def job_posts(bear):
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    files = sorted(p for p in POSTS.glob("*.md"))
    for f in files:
        meta, body = parse(f)
        payload = {
            "title": meta["title"],
            "slug": meta["slug"],
            "content": body,
            "publish": meta.get("publish", "true") != "false",
            "published_date": meta["date"],
            "tags": meta.get("tags", []),
            "lang": meta.get("lang", "en"),
        }
        if meta.get("meta_description"):
            payload["meta_description"] = meta["meta_description"]
        digest = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
        known = state.get(meta["slug"])
        if known and known.get("hash") == digest:
            continue
        if known:
            bear.call("PATCH", f"post/{known['uid']}/", payload)
            print(f"updated   {meta['slug']}")
            known["hash"] = digest
        else:
            r = bear.call("POST", "post/", payload)
            print(f"published {meta['slug']} -> {r.get('url')}")
            state[meta["slug"]] = {"uid": r.get("uid"), "hash": digest}
        time.sleep(1.1)
    if not bear.dry_run:
        STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n")


def job_blog(bear):
    cfg = json.loads((HERE / "blog.json").read_text(encoding="utf-8"))
    bear.call("PATCH", "blog/", cfg)
    print("Blog settings updated:", ", ".join(cfg))


def main():
    args = sys.argv[1:]
    mode = next((a for a in args if not a.startswith("--")), "posts")
    key, sub = os.environ.get("BEAR_API_KEY", ""), os.environ.get("BEAR_SUBDOMAIN", "")
    if not key or not sub:
        raise SystemExit("BEAR_API_KEY and BEAR_SUBDOMAIN must be set.")
    bear = Bear(sub, key, dry_run="--dry-run" in args)
    {"posts": job_posts, "blog": job_blog}[mode](bear)


if __name__ == "__main__":
    main()
