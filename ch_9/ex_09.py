fname = input('Enter file: ')
if len(fname) < 1: fname = 'clown.txt'
hand = open(fname)

di = dict()
for line in hand:
    words = line.rstrip().split()
    for word in words:
        di[word] = di.get(word, 0) + 1

largest = -1
theword = None
for w, i in di.items():
    if i > largest:
        largest = i
        theword = w

print(largest, theword)