fname = input('Enter file: ')
if len(fname) < 1: fname = 'clown.txt'
hand = open(fname)

di = dict()
for line in hand:
    words = line.rstrip().split()
    for word in words:
        di[word] = di.get(word, 0) + 1

tmp = list()
for k,v in di.items():
    g = (v,k)
    tmp.append(g)

tmp = sorted(tmp, reverse=True)
print(tmp[:5])