from urllib.request import urlopen
from bs4 import  BeautifulSoup
html = urlopen("https://book.zongheng.com/chapter/1276240/72489895.html")
bsObj = BeautifulSoup(html,features="lxml")

namelist = bsObj.findAll("div",{"class":"content"})
for name in namelist:
	print(name.get_text())