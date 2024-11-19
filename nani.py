han = open('mbox.txt')
for line in han:
    line = line.rstrip()
    wds = line.split()
    print(wds)
    if len(wds)==0:
        continue
    if wds[0]!='From':
        continue
    print(wds[2])