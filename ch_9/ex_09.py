fname = input('Enter file: ')
if len(fname) < 1: fname = 'clown.txt'
hand = open(fname)

for line in hand:
    line = line.rstrip()
    #  strip all spaces intro
    # print(line)
    words = line.split()
    # if len(words)>0:
    #     print(words[0])
    for word in words:
        print(word)