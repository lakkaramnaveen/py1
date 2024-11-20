import re
hand = open('mbox.txt')
y = "From: the beginning:, steve@ucmo.edu is it 12 or 19. Where are you From: I amm from india"
k = re.findall('[0-9]+', y)
k = re.findall('[ae]+', y)
k = re.findall('^F+?:', y) # non greedy
k = re.findall('\S+@\S+', y)
print(k)