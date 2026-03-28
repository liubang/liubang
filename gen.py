#!/usr/bin/env python

from datetime import datetime
from email.utils import parsedate_to_datetime
import os
from urllib.request import urlopen
import xml.etree.ElementTree as ET


BLOG_RSS_URL = "https://liubang.github.io/blog/index.xml"
BLOG_ARCHIVE_URL = "https://liubang.github.io/blog/archives/"
BLOG_URL = "https://liubang.github.io/blog/"
GITHUB_URL = "https://github.com/liubang"
ASSET_VERSION = os.environ.get("README_ASSET_VERSION", "1")


def fetch_blog_posts():
    with urlopen(BLOG_RSS_URL, timeout=10) as response:
        feed = response.read().decode("utf-8")
    root = ET.fromstring(feed).find("channel")
    posts = []
    for entry in root.findall("item")[:5]:
        posts.append(
            {
                "title": entry.find("title").text,
                "url": entry.find("link").text,
                "published": format_date(entry.find("pubDate").text),
            }
        )
    return posts


def format_date(value):
    try:
        return parsedate_to_datetime(value).strftime("%Y-%m-%d")
    except ValueError:
        return datetime.fromisoformat(value).strftime("%Y-%m-%d")


posts = fetch_blog_posts()

with open("README.md", "w") as f:
    f.write(
        """# Liubang

Backend / Storage / Testing / C++

I build and write about backend systems, storage-related topics, and engineering quality.
Recent posts focus on Bloom Filters, fuzz testing, and algorithm problem solving.

## About Me
- Focus: backend infrastructure, storage systems, testing, and performance
- Tech: C++, Go, Python, Linux
- Writing: <https://liubang.github.io/blog/>
- Interests: Bloom Filter, fuzzing, distributed systems, developer tooling

## Latest Blog Posts
"""
    )

    for post in posts:
        f.write(f"- {post['published']} [{post['title']}]({post['url']})\n")

    f.write(
        f"""[View all posts]({BLOG_ARCHIVE_URL})

## Elsewhere
- GitHub: <{GITHUB_URL}>
- Blog: <{BLOG_URL}>

## Stats
![Stats](./profile/stats.svg?v={ASSET_VERSION})
![Lang](./profile/lang.svg?v={ASSET_VERSION})
"""
    )
