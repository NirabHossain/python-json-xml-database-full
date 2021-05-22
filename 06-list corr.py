fh = open('mbox.txt')
count = 0
for line in fh:
    lin=line.rstrip()
    word=lin.split()
    if len(word)<2 or word[0]!='From':
        continue 
    print(word[1])
    count=count+1

print("There were", count, "lines in the file with From as the first word")

