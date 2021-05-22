fname = '82-mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    man = pieces[1]
    email=man.split('@')[1]

