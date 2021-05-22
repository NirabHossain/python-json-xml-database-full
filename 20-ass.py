import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
#url='http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url='http://py4e-data.dr-chuck.net/known_by_Korbyn.html'
repeat=7
loc=18

for x in range(repeat):
    url=urllib.request.urlopen(url).read()
    soup=BeautifulSoup(url,'html.parser')
    tags=soup('a')
    url=tags[loc-1].get('href',None)
y=re.findall('([^_]+)\.html',url)
print(y[0])



