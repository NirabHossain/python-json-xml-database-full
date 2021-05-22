import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#url=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.html').read()
url=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_791350.html').read()

soup=BeautifulSoup(url,'html.parser')

tags=soup('span')

#[print(int(tag.contents[0])) for tag in tags]
print(sum([int(tag.contents[0]) for tag in tags]))
    
