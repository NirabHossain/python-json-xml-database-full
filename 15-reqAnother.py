import urllib.request, urllib.parse, urllib.error
hand=urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
for lines in hand:
    print(lines.decode().rstrip())