fhand=open('81-count.txt')

name=dict()


for lines in fhand:
    line=lines.split()
    for word in line:
        name[word]=name.get(word,0)+1

ic=0
wrd=0
for aa,bb in name.items():
    if ic<bb:
        ic=bb
        wrd=aa

print(wrd,ic)