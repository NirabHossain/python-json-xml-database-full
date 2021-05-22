import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url=urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Fikret.html').read()


soup=BeautifulSoup(url,'html.parser')
tags=soup('a')
for tag in tags:
    print(tag.get('href',None))
