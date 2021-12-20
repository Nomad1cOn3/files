evens1 = []
odds1 = []
def evens():
    for x in range(1,51):
        if x%2==0: 
            evens1.append(x)
def odds():
    for y in range(1,51):
        if y not in evens1:
            odds1.append(y)
        
evens()
odds()
print(evens1)
print(odds1)