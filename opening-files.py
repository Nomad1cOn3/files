import os,random
l1 = input('File Name: ')
with open('numbers.txt') as f:
    numbers = f.readlines()
#numindex = random.randint(1, len(numbers)-1)
#print(numbers[:100])
for line in numbers:
    if line.startswith('843'):
        numbers = line.strip()
print(numbers)