from urllib.error import HTTPError
from urllib.request import urlopen

from bs4 import BeautifulSoup


def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsobj = BeautifulSoup(html.read(), features='lxml')
		title = bsobj.h1
	except AttributeError as e:
		return None
	return title


title = getTitle("http://www.pythonscraping.com/pages/warandpeace.html")
if title == None:
	print("Title could not be found")
else:
	print(title)
