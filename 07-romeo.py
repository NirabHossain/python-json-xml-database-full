fhand=open('romeo.txt')
lst=list()
for line in fhand:
    wds=line.split()
    for word in wds:
        if word in lst: continue
        lst.append(word)
lst.sort()
print(lst)
