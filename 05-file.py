fh = open('mbox.txt')
count = 0
for line in fh:
    if not line.startswith('From'):continue
    print(line)
    

print("There were", count, "lines in the file with From as the first word")

