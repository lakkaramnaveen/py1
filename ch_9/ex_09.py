fname = input('Enter file: ')
if len(fname) < 1: fname = 'clown.txt'
hand = open(fname)

for line in hand:
    print(line)