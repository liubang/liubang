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

Distributed Storage Engineer

I focus on building distributed storage systems and backend infrastructure, with an emphasis on reliability, performance, and engineering simplicity.
My work is centered on large-scale systems, and I am particularly interested in the design and implementation of distributed storage and distributed computing platforms.

## About Me
- Focus: distributed storage, distributed computing, backend infrastructure, and performance engineering
- Primary language: C++, with Go and Java as secondary tools
- Interests: system design, storage architecture, reliability engineering, and performance optimization
- Writing: <https://liubang.github.io/blog/>

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
