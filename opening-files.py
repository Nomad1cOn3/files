import os,random
l1 = input('File Name: ')
with open('numbers.txt') as f:
    numbers = f.readlines()
with open('sowpods.txt') as f:
    words = f.readlines()
#numindex = random.randint(1, len(numbers)-1)
#print(numbers[:100])
if l1 == 'numbers.txt':
    for line in numbers:
        if line.startswith('843'):
            numbers = line.rstrip()
    words = None
elif l1 == 'sowpods.txt':
    for line in words:
        if line.startswith('Cool'):
            words = line.rstrip()
    numbers = None
if words != None:
    print(words)
else:
    print(numbers)