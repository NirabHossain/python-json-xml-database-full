name = "mbox.txt"#input("Enter file:")
#if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dic=dict()

for lines in handle:
    line=lines.rstrip()
    words=line.split()
    if len(words)<6 or words[0]!='From': continue
    hour=words[5].split(':')
    hour=hour[0]
    dic[hour]=dic.get(hour,0)+1

lst=sorted([(aa,bb) for (aa,bb) in dic.items()])
#lst=list()
#for aa,bb in dic.items():
#    lst.append((aa,bb))
#lst=sorted(lst)
for aa,bb in lst:
    print(aa,bb)

