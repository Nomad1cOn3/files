#method 1
import math
x = lambda x: math.sqrt(x)
print(x(13689))

#method 2
def sq(num1):
  print(math.sqrt(num1))
sq(13689)

#method 3
def sq2(num2):
  return math.sqrt(num2)
print(sq2(13689))

#method 4
def sq3():
  print(math.sqrt(13689))
sq3()

#method 5
def sq4():
  return math.sqrt(13689)
print(sq4())