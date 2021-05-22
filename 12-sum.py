import re
print(sum([int(n) for n in re.findall('[0-9]+',open('86-Givendata.txt').read())]))

