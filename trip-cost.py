def hotel_cost(night):
  return(night*140)
def plane_ride_cost(city):
  if city == "Charlotte":
    return(183)
  if city == "Tampa":
    return(220)
  if city == "Pittsburgh":
    return(222)
  if city == "Los_Angeles":
    return(475)
def rental_car_cost(days):
  if days < 3:
    return(days*40) 
  elif days >= 7:
    return((days*40) - 50)
  else:
    return((days*40)-20)
def trip_cost(spending_money, night, days, city):
  l = hotel_cost(night)+plane_ride_cost(city)+rental_car_cost(days)+spending_money
  print('total cost is',l)
  return(l)
night = int(input("how many nights? "))
days = int(input("How many days will you rent? "))
city = str(input("what city? "))
spending_money = int(input("How much spending money? "))
trip_cost(spending_money,night,days,city)