list1 = []
list2 = []
l = None
for x in range(1,10):
    try:
        l = input()
        l = int(l)
        list1.append(l)
    except:
        list2.append(l)
print(sorted(list1))
print(sorted(list2)) 