fhand=open('mbox.txt')
ic=0
iw=0
name=dict()
for lines in fhand:
    line=lines.rstrip()
    words=line.split()

    if len(words)<2 or words[0]!='From': continue
    #print(line)
    name[words[1]]=name.get(words[1],0)+1

for aa,bb in name.items(): 
    if ic<bb:
        ic=bb
        iw=aa

print(iw,ic)    
