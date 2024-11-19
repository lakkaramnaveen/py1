counts = dict()

print('Enter a line of text: ')
line = input('')
names = line.split()

for name in names:
        counts [name] = counts.get(name,0) + 1

print (counts)