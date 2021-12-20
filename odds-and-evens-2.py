evens1 = []
odds1 = []
index = 0
def evens():
    for x in range(1,51):
        if x%2==0: 
            evens1.append(x)
def odds():
    for y in evens1:
        global index
        odds1.append(evens1[index]-1)
        index = index+1     
evens()
odds()
print(evens1)
print(odds1)
