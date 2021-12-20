import os,random
numbers = None
with open(numbers.txt) as f:
    numbers = f.readlines()
print(numbers[1,len(numbers)-1])
