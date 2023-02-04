import bs4
exampleFile = open('data/example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')
print(type(exampleSoup))
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(str(elems[0]))
a = elems[0].getText()
print(elems[0].getText())
print(elems[0].attrs)

