import requests
import xml.etree.ElementTree as ET

feed = requests.get('https://iliubang.cn/feed.xml').text
root = ET.fromstring(feed)
nsfeed = {'nsfeed': 'http://www.w3.org/2005/Atom'}
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
    for entry in root.findall('nsfeed:entry', nsfeed)[:5]:
        text = entry.find('nsfeed:title', nsfeed).text
        url = entry.find('nsfeed:link', nsfeed).attrib['href']
        published = entry.find('nsfeed:published', nsfeed).text[:10]
        f.write('- {} [{}]({})\n'.format(published, text, url))
        
    f.write(''' 
[>>> More blog posts](https://iliubang.cn/archive.html)

## Statistics
![Stats](https://github-readme-stats.vercel.app/api?username=liubang&show_icons=true&count_private=true&hide_title=true&hide=issues&line_height=24)
![Lang](https://github-readme-stats.vercel.app/api/top-langs/?username=liubang&layout=compact&hide_title=true&langs_count=6)
''')
