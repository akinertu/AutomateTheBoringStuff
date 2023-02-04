#! python3
# searchpypi.py  - Opens several search results.

import requests, webbrowser, bs4

res = requests.get('https://pypi.org/search/?q=' 
+ 'asd')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('.package-snippet')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)