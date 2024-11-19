fname = input('Enter file: ')
if len(fname) < 1: fname = 'clown.txt'
hand = open(fname)

di = dict()
for line in hand:
    line = line.rstrip()
    #  strip all spaces intro
    words = line.split()
    for word in words:
        # if the key is not there then the count is zero
        # if the word is not in "di" then assign it zero
        di[word] = di.get(word, 0) + 1

for w, i in di.items():
    print(w, i)