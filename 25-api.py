import urllib.request, urllib.parse, urllib.error
import json
url='http://py4e-data.dr-chuck.net/json?'

address=input('Location:')
url=url+urllib.parse.urlencode({'address':address})

print('Retrieving',url)
uh=urllib.request.urlopen(url)
data=uh.read().decode()
print('Retrieved:',len(data),'characters')

try:
    js=json.loads(data)
except:
    js=None

if not js or 'status' not in js or js['status']!='OK':
    print('Failure to retrieve')


#API key: AIzaSyDS4Iu2wHggAdNRREiBitbbff5Rx5Ah_2k 