l1 = input('File Name: ')
with open('mbox-short.txt') as mbox:
    mbox = mbox.readlines()
index = 1
if l1 == 'mbox-short.txt':
    for line in mbox:
        index = index+1
        print(mbox[index-1])