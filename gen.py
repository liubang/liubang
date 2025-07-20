#!/usr/bin/env python
import requests
import xml.etree.ElementTree as ET

feed = requests.get('https://liubang.github.io/blog/index.xml').text
root = ET.fromstring(feed).find('channel')
# http://patorjk.com/software/taag/#p=display&f=Bloody&t=Liubang
with open('README.md', 'w') as f:
    f.write(r''' 
```
 ██▓     ██▓ █    ██  ▄▄▄▄    ▄▄▄       ███▄    █   ▄████ 
▓██▒    ▓██▒ ██  ▓██▒▓█████▄ ▒████▄     ██ ▀█   █  ██▒ ▀█▒
▒██░    ▒██▒▓██  ▒██░▒██▒ ▄██▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░
▒██░    ░██░▓▓█  ░██░▒██░█▀  ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓
░██████▒░██░▒▒█████▓ ░▓█  ▀█▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒
░ ▒░▓  ░░▓  ░▒▓▒ ▒ ▒ ░▒▓███▀▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ 
░ ░ ▒  ░ ▒ ░░░▒░ ░ ░ ▒░▒   ░   ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ 
  ░ ░    ▒ ░ ░░░ ░ ░  ░    ░   ░   ▒      ░   ░ ░ ░ ░   ░ 
    ░  ░ ░     ░      ░            ░  ░         ░       ░ 
                           ░
```
## Latest blog posts
''')
    for entry in root.findall('item')[:5]:
        text = entry.find('title').text
        url = entry.find('link').text
        published = entry.find('pubDate').text
        f.write('- {} [{}]({})\n'.format(published, text, url))

    f.write(''' 
[>>> More blog posts](https://liubang.github.io/blog/archives/)

## Stats
![Stats](https://github-readme-stats.vercel.app/api?username=liubang&show_icons=true&count_private=true&hide_title=true&hide=issues&line_height=24&theme=onedark)
![Lang](https://github-readme-stats.vercel.app/api/top-langs/?username=liubang&layout=compact&hide_title=true&langs_count=6&theme=onedark&card_width=280&hide=scss,html,javascript,shell,Emacs%20Lisp,Vim%20script)
''')
