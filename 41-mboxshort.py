fh=open('82-mbox-short.txt')
lst=dict()
for hand in fh:
    lines=hand.rstrip().split()
    if(len(lines)<6 or lines[0]!="From"): continue
    h=lines[5].split(':')[0]
    lst[h]=lst.get(h,0)+1

makeList=sorted([(aa,bb) for aa,bb in lst.items()])
for aa,bb in makeList: print(aa,bb)
