def distance_from_zero(a_number):
  try:
    a_number = float(a_number)
    absans = abs(a_number)
    return(absans)
  except:
    return('Nope')
a_number = input('Enter a number: ')
absans = distance_from_zero(a_number)
print(absans)