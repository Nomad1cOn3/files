l1 = input('File Name: ')
index = 1
try: 
    f = open('mbox-short.txt',mode='r')
    if l1 == 'mbox-short.txt':
        for line in mbox:
            index = index+1
            print(mbox[index-1])
finally:
    f.close()