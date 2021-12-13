import time
 
y = int(input())
for x in range(100 - y):
  y = y+1
  print(y)
  time.sleep(.03)