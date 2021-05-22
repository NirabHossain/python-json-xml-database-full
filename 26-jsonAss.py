import urllib.request, urllib.parse, urllib.error
import json

#url=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.json')
url=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_791353.json')
data=url.read()
info=json.loads(data)

ic=0
for x in info["comments"]:
    ic=ic+int(x["count"])
print(ic)