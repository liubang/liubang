#!/usr/bin/env python

from email.utils import parsedate_to_datetime
from urllib.request import urlopen
import xml.etree.ElementTree as ET


with urlopen("https://liubang.github.io/blog/index.xml", timeout=10) as response:
    feed = response.read().decode("utf-8")
root = ET.fromstring(feed).find("channel")

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

    for entry in root.findall("item")[:5]:
        title = entry.find("title").text
        url = entry.find("link").text
        published = parsedate_to_datetime(entry.find("pubDate").text).strftime(
            "%Y-%m-%d"
        )
        f.write(f"- {published} [{title}]({url})\n")

    f.write(
        """

[View all posts](https://liubang.github.io/blog/archives/)

## Elsewhere
- GitHub: <https://github.com/liubang>
- Blog: <https://liubang.github.io/blog/>

## Stats
![Stats](https://github-readme-stats.vercel.app/api?username=liubang&show_icons=true&count_private=true&hide_title=true&hide=issues&line_height=24&theme=onedark)
![Lang](https://github-readme-stats.vercel.app/api/top-langs/?username=liubang&layout=compact&hide_title=true&langs_count=6&theme=onedark&card_width=280&hide=scss,html,javascript,shell,Emacs%20Lisp,Vim%20script)
"""
    )
