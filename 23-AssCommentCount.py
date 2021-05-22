import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
url=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_791352.xml')
data=url.read()
tree=ET.fromstring(data)
lst=tree.findall('comments/comment/count')

print(sum([int(x.text) for x in lst]))
    
    