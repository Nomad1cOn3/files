import time

print('Hello!')
print(' ')
time.sleep(.5)
print('Welcome to the Calculator!')
print(' ')

i = '0'
i2 = 'y'
tupley = 'y'
tuplen = 'n'
tupleopadd = ('Add','add','+')
tupleopsubtract = ('Subtract','subtract','minus','Minus','-')
tupleopmult = ('Multiply','multiply','X','x','*')
tupleopdivide = ('Divide','divide','/','÷')
op = '0'
num1 = int(0)
num2 = int(0)
x = int(0)

time.sleep(1)
while i == 'n' or '0': 
  if i2 == 'n':
    i = input('Are you sure?(y/n): ')
    if i == 'y':
      break
    
    elif i == 'n':
      i2 = 'y'
      continue

  elif i2 == 'y':
    print(' ')
    num1 = int(input('Enter the first number: '))
    print(' ')
    time.sleep(.4)
    num2 = int(input('Enter the second number: '))
    print(' ')
    time.sleep(.4)

    while i2 == '0' or 'y':
      op = input('What Operation would you like to preform?(+ - * ÷): ')
      print(' ')
      print(' ')

      if op in tupleopadd:
        x = int(num1)+int(num2)
        print('The result is:', x)
        print(' ')
        time.sleep(1)
        i2 = input('Would you like to calculate anything else?(y/n): ')
        if i2 == 'n':
          i = 'n'
          break
        elif i2 == 'y':
          break
      
      elif op in tupleopsubtract:
        x = int(num1)-int(num2)
        print('The result is:', x)
        print(' ')
        time.sleep(1)
        i2 = input('Would you like to calculate anything else?(y/n): ')
        if i2 == 'n':
          i = 'n'
          break
        elif i2 == 'y':
          break

      elif op in tupleopmult:
        x = int(num1)*int(num2)
        print('The result is:', x)
        print(' ')
        time.sleep(1)
        i2 = input('Would you like to calculate anything else?(y/n): ')
        if i2 == 'n':
          i = 'n'
          break
        elif i2 == 'y':
          break

      elif op in tupleopdivide:
        x = int(num1)/int(num2)
        print('The result is:', x)
        print(' ')
        time.sleep(1)
        i2 = input('Would you like to calculate anything else?(y/n): ')
        if i2 == 'n':
          i = 'n'
          break
        elif i2 == 'y':
          break

      else:
        print('Invalid Operation: Please Try Again')
        print(' ')
        time.sleep(1)
        continue