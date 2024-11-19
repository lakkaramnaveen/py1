fname = input('Enter file: ')
if len(fname) < 1: fname = 'clown.txt'
hand = open(fname)

for line in hand:
    line = line.rstrip()
    #  strip all spaces intro
    # print(line)
    words = line.strip()
    if len(words)>0:
        print(words[0])