# hand = open('mbox.txt')
# for line in hand:
#     line = line.rstrip ()
#     if line.find('From: ') >= 0:
#         print (line)

hand = open('mbox.txt')
for line in hand:
    line = line.rstrip ()
    if line.startswith('From: '):
        print (line)

# import re

# hand = open('mbox.txt')
# for line in hand:
#     line = line.rstrip ()
#     if re.search('^From: ', line):
#         print (line)