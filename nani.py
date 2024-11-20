import re
hand = open('mbox.txt')
# for line in hand:
#     line = line.rstrip ()
#     if re.search('^X-\S+:', line):
#         print (line)
y = "hi how are you doing today what is the time is it 12 or 19"
k = re.findall('[0-9]+', y)
print(k)