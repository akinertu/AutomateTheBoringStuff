#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

#TODO Loads the XKCD home page
import requests, bs4, os

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)    # store comics in ./xkcd

while not url.endswith('#'):
    print('Downloading page %s...' % url)
    resource = requests.get(url) #download site
    resource.raise_for_status()
    soup = bs4.BeautifulSoup(resource.text, 'html.parser')
    comicUrl = 'https:' + soup.select('#comic img')[0].get('src')
    print('Downloading image %s...' % (comicUrl))
    comicFile = requests.get(comicUrl)
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in comicFile.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    url = 'https://xkcd.com' + soup.select('a[rel="prev"]')[0].get('href')
    
print('Done.')

