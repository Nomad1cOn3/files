#method 1
def cube(number):
  number = number**3
  return(number)
def by_three(number):
  divisible = bool(number%3 == 0)
  if divisible == True:
    number = cube(number)
    return(number)
  else:
    return(False)
number = int(input('Enter a number divisble by three to cube: '))
number = by_three(number)
print(number)

#method 2 - doesn't work yet
#number = 0
#class cube:
#  def __init__(self,number):
#    divisible = bool(number%3 == 0)
#    if divisible == True:
#      number = cube(number)
#    else:
#      return(None)
#  def cube(self,number):
#    number = number**3
#    return(number)

#p1 = cube(number)
#p1.cube(3)