import time
hours = 0
medhours = 0
rate = 0
rate2 = 0
medpay = 0
medpay2 = 0
pay = 0

i = 'y'

def computepay():
  if hours > 40:
    rate2 = float(rate)*1.5
    medhours = float(hours)-40
    medpay = 40*float(rate)
    medpay2 = float(medhours)*rate2
    pay = float(medpay2)+float(medpay)
    print('Your total gross pay is', pay)

  elif hours <= 40:
    pay = float(hours)*float(rate)
    print('Your total gross pay is', pay)

while i == '0' or 'y':
  rate = float(input('Current pay rate?: '))
  hours = float(input('How many hours?: '))
  computepay()
  print(' ')
  time.sleep(.8)
  i = input('Would you like to preform another calculation?(y/n): ')
  if i == 'y':
    print(' ')
    continue
  elif i == 'n':
    break