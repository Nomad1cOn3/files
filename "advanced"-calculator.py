import time
import math

w = '0'
x = '1'
y = True
z = None
q = '0'
i = '0'
i2 = 'y'
i3 = 'start'
i4 = '0'
i5 = '0'
i6 = '0'
i7 = '0'
i8 = '0'
i9 = '0'
i10 = '0'
i11 = '0'
i12 = '0'
i13 = '0'
i14 = '0'
i15 = '0'
i16 = '0'
i17 = '0'
i18 = '0'
i19 = '0'
i20 = '0'
i21 = '0'
i22 = '0'
i23 = '0'
i24 = '0'
i25 = '0'
i26 = '0'
i27 = '0'
i28 = '0'
i29 = '0'
i30 = '0'
i31 = '0'
i32 = '0'
i33 = '0'
i34 = '0'
i35 = '0'
ierror = '0'
compareyes = '0'
trigop = '0'

def menu():
  print(' ')
  time.sleep(1)
  print('--------- Menu ---------')
  print(' ')
  time.sleep(.3)
  print('1. Simple Mode(default)')
  print(' ')
  time.sleep(.3)
  print('2. Complex Mode(beta)')
  print(' ')
  time.sleep(.3)
  print('Or Type "esc" to quit')
  print(' ')
  time.sleep(.3)
  print('----------- 0 -----------')
  print(' ')
  print(' ')
  time.sleep(.5)

def opmenu():
  print(' ')
  time.sleep(1)
  print('------ Operator Syntax ------')
  print(' ')
  time.sleep(.3)
  print('Addition: +')
  print(' ')
  time.sleep(.3)
  print('Subtraction: -')
  print(' ')
  time.sleep(.3)
  print('Multiplacation: *')
  print(' ')
  time.sleep(.3)
  print('Division: ÷')
  print(' ')
  time.sleep(.3)
  print('Exponentiation: ^')
  print(' ')
  time.sleep(.3)
  print('Compare: >')
  print(' ')
  time.sleep(.3)
  print('Trignometrics: º')
  print(' ')
  time.sleep(.3)
  print('------------- 0 -------------')
  print(' ')
  print(' ')

def comparemenu():
  print(' ')
  time.sleep(1)
  print('------ Compare Menu ------')
  print(' ')
  time.sleep(.3)
  print('Check True: Checks if a statement is true: 1')
  print(' ')
  time.sleep(.3)
  print(' ')
  time.sleep(.3)
  print('------------ 0 ------------')

def trigmenu():
  print(' ')
  time.sleep(1)
  print('-------- Trig Menu --------')
  print(' ')
  time.sleep(.3)
  print('Calculator is in degree mode.')
  print(' ')
  time.sleep(.3)
  print('1. Sine')
  print(' ')
  time.sleep(.3)
  print('2. Cosine')
  print(' ')
  time.sleep(.3)
  print('3. Tangent')
  print(' ')
  time.sleep(.3)
  print('Or type "esc" to quit ')
  print('------------ 0 ------------')

def locationerror():
  print('Invalid Location: Redirecting')
  print(' ')
  time.sleep(.2)
  print('Invalid Location: Redirecting .')
  print(' ')
  time.sleep(.2)
  print('Invalid Location: Redirecting . .')
  print(' ')
  time.sleep(.2)
  print('Invalid Location: Redirecting . . .')
  print(' ')
  time.sleep(.2)
  #ierror = '1'

def sinmenu():
  print('---------- Sine ----------')
  print(' ')
  time.sleep(.3)
  print('Sine finds the value of the side opposite a given angle in a right triangle. The default value of the hypotenuse is 1. ')
  print(' ')
  time.sleep(.3)
  print('------------ 0 ------------')

def cosmenu():
  print('---------- Cosine ----------')
  print(' ')
  time.sleep(.3)
  print('Cosine finds the value of the side adjacent a given angle in a right triangle. The default value of the hypotenuse is 1. ')
  print(' ')
  time.sleep(.3)
  print('------------ 0 ------------')

def tanmenu():
  print('---------- Tangent ----------')
  print(' ')
  time.sleep(.3)
  print('Tangent finds the value of the side opposite a given angle in a right triangle divided by the adjacent side. ')
  print(' ')
  time.sleep(.3)
  print('------------- 0 -------------')

def fourohfour():
  print(' ')
  time.sleep(.1)
  print('══██████░░══██████░░══██████░░══██████░░══██████░░')
  print('░░══██████░░══██████░░══██████░░══██████░░══██████')
  print(' ')
  time.sleep(.1)
  print('██░░══██████░░══██████░░══██████░░══██████░░══████')
  print(' ')
  time.sleep(.1)
  print('████░░══██████░░══██████░░══██████░░══██████░░══██')
  print(' ')
  time.sleep(.1)
  print('██████░░══██████░░══██████░░══██████░░══██████░░══')
  print(' ')
  time.sleep(.1)
  print('══██████░░══██████░░══██████░░══██████░░══██████░░')
  print('░░══██████░░══██████░░══██████░░══██████░░══██████')
  print(' ')
  time.sleep(.1)
  print('██░░══██████░░══██████░░══██████░░══██████░░══████')
  print(' ')
  time.sleep(.1)
  print('████░░══██████░░══██████░░══██████░░══██████░░══██')
  print(' ')
  time.sleep(.1)
  print('██████░░══██████░░══██████░░══██████░░══██████░░══')
  print(' ')
  time.sleep(.1)
  print('══██████░░══██████░░══██████░░══██████░░══██████░░')
  print('░░══██████░░══██████░░══██████░░══██████░░══██████')
  print(' ')
  time.sleep(.1)
  print('██░░══██████░░══██████░░══██████░░══██████░░══████')
  print(' ')
  time.sleep(.1)
  print('████░░══██████░░══██████░░══██████░░══██████░░══██')
  print(' ')
  time.sleep(.1)
  print('██████░░══██████░░══██████░░══██████░░══██████░░══')
  print(' ')
  time.sleep(.1)
  print('══██████░░══██████░░══██████░░══██████░░══██████░░')
  print('░░══██████░░══██████░░══██████░░══██████░░══██████')
  print(' ')
  time.sleep(.1)
  print('██░░══██████░░══██████░░══██████░░══██████░░══████')
  print(' ')
  time.sleep(.1)
  print('████░░══██████░░══██████░░══██████░░══██████░░══██')
  print(' ')
  time.sleep(.1)
  print('██████░░══██████░░══██████░░══██████░░══██████░░══')
  print(' ')
  time.sleep(.1)
  print('══██████░░══██████░░══██████░░══██████░░══██████░░')
  print('░░══██████░░══██████░░══██████░░══██████░░══██████')
  print(' ')
  time.sleep(.1)
  print('██░░══██████░░══██████░░══██████░░══██████░░══████')
  print(' ')
  time.sleep(.1)
  print('████░░══██████░░══██████░░══██████░░══██████░░══██')
  print(' ')
  time.sleep(.1)
  print('██████░░══██████░░══██████░░══██████░░══██████░░══')
  print(' ')
  time.sleep(.5)
  print('You found a secret!')
  time.sleep(.5)


def add():
  while i14 == '0':
    try:
      num1 = float(input('Enter a number: '))
      print(' ')
      time.sleep(.5)
      break
      
    except ValueError:
      print(' ')
      time.sleep(.5)
      print('Invalid Input')
      print(' ')
      time.sleep(.5)
      continue

  while i15 == '0':
      try:
        num2 = float(input('Enter another number: '))
        print(' ')
        x = (num1)+(num2)
        time.sleep(.5)
        break

      except ValueError:
        print(' ')
        time.sleep(.5)
        print('Invalid Input')
        print(' ')
        time.sleep(.5)
        continue
      
  print('The result is:', x)
  print(' ')
      
def sub():
  while i16 == '0':
    try:
      num1 = float(input('Enter a number: '))
      print(' ')
      time.sleep(.5)
      break
      
    except ValueError:
      print(' ')
      time.sleep(.5)
      print('Invalid Input')
      print(' ')
      time.sleep(.5)
      continue

  while i17 == '0':
      try:
        num2 = float(input('Enter another number: '))
        print(' ')
        x = (num1)-(num2)
        time.sleep(.5)
        break

      except ValueError:
        print(' ')
        time.sleep(.5)
        print('Invalid Input')
        print(' ')
        time.sleep(.5)
        continue

  print('The Result is:',x)
  print(' ')

def mult():
  while i18 == '0':
    try:
      num1 = float(input('Enter a number: '))
      print(' ')
      time.sleep(.5)
      break
      
    except ValueError:
      print(' ')
      time.sleep(.5)
      print('Invalid Input')
      print(' ')
      time.sleep(.5)
      continue

  while i19 == '0':
      try:
        num2 = float(input('Enter another number: '))
        print(' ')
        x = (num1)*(num2)
        time.sleep(.5)
        break

      except ValueError:
        print(' ')
        time.sleep(.5)
        print('Invalid Input')
        print(' ')
        time.sleep(.5)
        continue

  print('The product is:', x)
  print(' ')
  
def div():
  while i20 == '0':
    try:
      num1 = float(input('Enter a number: '))
      print(' ')
      time.sleep(.5)
      break
      
    except ValueError:
      print(' ')
      time.sleep(.5)
      print('Invalid Input')
      print(' ')
      time.sleep(.5)
      continue

  while i21 == '0':
      try:
        num2 = float(input('Enter another number: '))
        print(' ')
        x = (num1)/(num2)
        time.sleep(.5)
        break

      except ValueError:
        print(' ')
        time.sleep(.5)
        print('Invalid Input')
        print(' ')
        time.sleep(.5)
        continue

  print('The quotient is:', x)
  print(' ')

def exp():
  while i22 == '0':
    try:
      num1 = float(input('Enter a number: '))
      print(' ')
      time.sleep(.5)
      break
      
    except ValueError:
      print(' ')
      time.sleep(.5)
      print('Invalid Input')
      print(' ')
      time.sleep(.5)
      continue

  while i23 == '0':
      try:
        num2 = float(input('Enter another number: '))
        print(' ')
        x = (num1)**(num2)
        time.sleep(.5)
        break

      except ValueError:
        print(' ')
        time.sleep(.5)
        print('Invalid Input')
        print(' ')
        time.sleep(.5)
        continue
  print('The result is:', x)
  print(' ')

def comp():
  while i5 == '0':
      i11 = '0'
      while i11 == '0':
        try:
          num1 = float(input('Enter a number: '))
          print(' ')
          time.sleep(.5)
          break

        except ValueError:
          print(' ')
          time.sleep(.5)
          print('Invalid Input')
          print(' ')
          time.sleep(.5)
          continue
        
      while i12 == '0':
        try:
          compareyes = input('Comparison Sign?(>,<,≥,≤,=): ')
          print(' ')
          time.sleep(.5)
          if compareyes == '>':
            break
          elif compareyes == '<':
            break
          elif compareyes == '≤':
            break
          elif compareyes == '≥':
            break
          elif compareyes == '=':
            break
          else:
            raise Exception

        except Exception:
          print('Invalid Input')
          print(' ')
          time.sleep(.5)
          continue

      while i13 == '0':
        try:
          num2 = float(input('Enter a second number: '))
          print(' ')
          print(' ')
          time.sleep(.5)
          break

        except ValueError:
          print(' ')
          time.sleep(.5)
          print('Invalid Input')
          print(' ')
          time.sleep(.5)
          continue
        
      if compareyes == '>':
        print('Statement:',num1,'>',num2)
        print(' ')
        time.sleep(.5)
        y = bool(num1>num2)
        if y == True:
          print('Statement is True. ')
          break
        
        elif y == False:
          print('Statement is False.')
          break

      elif compareyes == '<':
        print('Statement:',num1,'<',num2)
        print(' ')
        time.sleep(.5)
        y = bool(num1<num2)
        if y == True:
          print('Statement is True. ')
          break
        
        elif y == False:
          print('Statement is False.')
          break

      elif compareyes == '≥':
        print('Statement:',num1,'≥',num2)
        print(' ')
        time.sleep(.5)
        y = bool(num1>=num2)
        if y == True:
          print('Statement is True. ')
          break
        
        elif y == False:
          print('Statement is False.')
          break

      elif compareyes == '≤':
        print('Statement:',num1,'≤',num2)
        print(' ')
        time.sleep(.5)
        y = bool(num1<=num2)
        if y == True:
          print('Statement is True. ')
          break
        
        elif y == False:
          print('Statement is False.')
          break

      elif compareyes == '=':
        print('Statement:',num1,'=',num2)
        print(' ')
        time.sleep(.5)
        y = bool(num1==num2)
        if y == True:
          print('Statement is True. ')
          break
        
        elif y == False:
          print('Statement is False.')
          break

      else:
        print('Invalid Comparison Sign: Please Try Again')
        print(' ')
        time.sleep(.5)
        continue

def trig():
  while i24 == '0':
    while i29 == '0':
      try: 
        trigmenu()
        print(' ')
        time.sleep(.5)
        trigop = input('Desired Operation?: ')
        if trigop == '1':
          print(' ')
          time.sleep(.5)
          sinmenu()
          print(' ')
          time.sleep(.5)
          while i30 == '0':
            try:
              num1 = int(input('Enter an angle value: '))
              print(' ')
              time.sleep(.5)
              break
            
            except ValueError:
              print(' ')
              time.sleep(.5)
              print('Invalid Input: Please Try Again')
              print(' ')
              time.sleep(.5)
              continue
          while i31 == '0':
            try:
              num2 = input('Enter the value of the hypotenuse(default value is 1): ')
              print(' ')
              time.sleep(.5)
              
              if len(num2) == 0:
                break
              
              else:
                num2 = int(num2)
                break
            
            except ValueError:
              if len(num2) == 0:
                break
              
              else:
                print(' ')
                time.sleep(.5)
                print('Invalid Input: Please Try Again')
                print(' ')
                time.sleep(.5)
                continue

          q = num1      
          num1 = math.radians((num1))
          x = math.sin((num1))
          while i32 == '0':
            if len(num2) > 0:
              x = x*num2
              break
            elif len(num2) == 0:
              break

          x = round(x,4)
          print('The sine of',q,'is',x)
          break
        
        elif trigop == '2':
          print(' ')
          time.sleep(.5)
          cosmenu()
          print(' ')
          time.sleep(.5)
          while i30 == '0':
            try:
              num1 = int(input('Enter an angle value: '))
              print(' ')
              time.sleep(.5)
              break
            
            except ValueError:
              print(' ')
              time.sleep(.5)
              print('Invalid Input: Please Try Again')
              print(' ')
              time.sleep(.5)
              continue
          while i31 == '0':
            try:
              num2 = input('Enter the value of the hypotenuse(default value is 1): ')
              print(' ')
              time.sleep(.5)
              
              if len(num2) == 0:
                break
              
              else:
                num2 = int(num2)
                break
            
            except ValueError:
              if len(num2) == 0:
                break
              
              else:
                print(' ')
                time.sleep(.5)
                print('Invalid Input: Please Try Again')
                print(' ')
                time.sleep(.5)
                continue

          q = num1      
          num1 = math.radians((num1))
          x = math.cos((num1))
          while i32 == '0':
            if len(num2) > 0:
              x = x*num2
              break
            elif len(num2) == 0:
              break

          x = round(x,4)
          print('The cosine of',q,'is',x)
          break

        elif trigop == '3':
          print(' ')
          time.sleep(.5)
          tanmenu()
          print(' ')
          time.sleep(.5)
        elif trigop == 'esc':
          break
        else:
         raise Exception
      
      except Exception:
        print(' ')
        time.sleep(.5)
        print('Invalid Operation: Please Try Again')
        print(' ')
        time.sleep(.5)
        continue

tupley = 'y'
tuplen = 'n'
tupleopadd = ('Add','add','+')
tupleopsubtract = ('Subtract','subtract','minus','Minus','-')
tupleopmult = ('Multiply','multiply','X','x','*')
tupleopdivide = ('Divide','divide','/','÷')
tupletrig = ('Trig','trig','trignometry','Trignometry','º')
op = '0'
compop = '0'
compareop = '0'
num1 = int(0)
num2 = int(0)

print('Hello!')
print(' ')
time.sleep(.5)
print('Welcome to the Calculator!')
print(' ')
while i8 == '0':
  try:
    while i7 == '0':
      if i3 == 'end':
        i3 = 'start'
        w = '0'
      menu()
      w = input('Would you like simple or complex mode?: ')
      if w == '2':
        w = 2
        break
      elif w == '1':
        w = 1
        break
      elif len(w) == 0:
        w = 1
        break
      elif w == 'esc':
        i10 = 'esc'
        w = int('esc')
      elif w == '404':
        w = 404
        fourohfour()
      else:
        z = bool(int(w))
        if z == True:
          if int(w) != 1 or 2:
            print(' ')
            time.sleep(.5)
            print('Invalid Input: Please Try Again')
            continue
        elif z == False:
          w = int(w)
          
    if w == 404:
      continue
    
    elif w == 1:
      while w == 1:  
        time.sleep(1)
        while i == 'n' or '0': 
          if i2 == 'n':
            i = input('Are you sure?(y/n): ')
            if i == 'y':
              w = '2'
              break
          
            elif i == 'n':
              i2 = 'y'
              continue

          elif i2 == 'y':
            print(' ')
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

    elif w == 2:
      while w == 2: 
        print(' ') 
        time.sleep(.5)
        if i3 == 'start':
          print(' ')
          opmenu()
          time.sleep(1)
          compop = input('Desired Operation?: ')
        
        elif i3 == 'y':
          print(' ')
          opmenu()
          time.sleep(1)
          compop = input('Desired Operation?: ')

        elif i3 == 'end':
          break

        if compop == '+':
          print(' ')
          time.sleep(.5)
          add()
          print(' ')
          time.sleep(1)
          while i27 == '0':
            try:
              i3 = input("Would you like to preform another calculation?(y/n): ")
            
              if i3 == 'n':
                i3 = 'end'
                break

              elif i3 == 'y':
                break

              else:
                raise Exception
            
            except Exception:
              print(' ')
              time.sleep(.5)
              print('Invalid Input: Please Try Again')
              print(' ')
              time.sleep(.5)
              continue

        elif compop == '-':
          print(' ')
          time.sleep(.5)
          sub()
          print(' ')
          time.sleep(1)
          while i27 == '0':
            try:
              i3 = input("Would you like to preform another calculation?(y/n): ")
            
              if i3 == 'n':
                i3 = 'end'
                break

              elif i3 == 'y':
                break

              else:
                raise Exception
            
            except Exception:
              print(' ')
              time.sleep(.5)
              print('Invalid Input: Please Try Again')
              print(' ')
              time.sleep(.5)
              continue

        elif compop == '*':
          print(' ')
          time.sleep(.5)
          mult()
          print(' ')
          time.sleep(1)
          while i27 == '0':
            try:
              i3 = input("Would you like to preform another calculation?(y/n): ")
            
              if i3 == 'n':
                i3 = 'end'
                break

              elif i3 == 'y':
                break

              else:
                raise Exception
            
            except Exception:
              print(' ')
              time.sleep(.5)
              print('Invalid Input: Please Try Again')
              print(' ')
              time.sleep(.5)
              continue

        elif compop == '÷':
          print(' ')
          time.sleep(.5)
          div()
          print(' ')
          time.sleep(1)
          while i27 == '0':
            try:
              i3 = input("Would you like to preform another calculation?(y/n): ")
            
              if i3 == 'n':
                i3 = 'end'
                break

              elif i3 == 'y':
                break

              else:
                raise Exception
            
            except Exception:
              print(' ')
              time.sleep(.5)
              print('Invalid Input: Please Try Again')
              print(' ')
              time.sleep(.5)
              continue

        elif compop == '^':
          print(' ')
          time.sleep(.5)
          exp()
          print(' ')
          time.sleep(1)
          while i27 == '0':
            try:
              i3 = input("Would you like to preform another calculation?(y/n): ")
            
              if i3 == 'n':
                i3 = 'end'
                break

              elif i3 == 'y':
                break

              else:
                raise Exception
            
            except Exception:
              print(' ')
              time.sleep(.5)
              print('Invalid Input: Please Try Again')
              print(' ')
              time.sleep(.5)
              continue

        elif compop == '>':
            i3 = '0'
            print(' ')
            time.sleep(.5)
            comparemenu()
            print(' ')
            time.sleep(.5)
            compareop = input('Desired Option?: ')
            print(' ')
            if compareop == '1':
              print(' ')
              time.sleep(.5)
              comp()
              print(' ')
              print(' ')
              time.sleep(1)
              while i27 == '0':
                try:
                  i3 = input("Would you like to preform another calculation?(y/n): ")
            
                  if i3 == 'n':
                    i3 = 'end'
                    break

                  elif i3 == 'y':
                    break

                  else:
                    raise Exception
            
                except Exception:
                  print(' ')
                  time.sleep(.5)
                  print('Invalid Input: Please Try Again')
                  print(' ')
                  time.sleep(.5)
                  continue

            else:
              print(' ')
              time.sleep(.5)
              print('Invalid Option: Please Try Again')
              continue
        
        elif compop in tupletrig:
          while i28 == '0':
            print(' ')
            time.sleep(.5)
            trig()
            print(' ')
            time.sleep(1)
            while i27 == '0':
                try:
                  i3 = input("Would you like to preform another calculation?(y/n): ")
            
                  if i3 == 'n':
                    i3 = 'end'
                    break

                  elif i3 == 'y':
                    break

                  else:
                    raise Exception
            
                except Exception:
                  print(' ')
                  time.sleep(.5)
                  print('Invalid Input: Please Try Again')
                  print(' ')
                  time.sleep(.5)
                  continue

        else:
          print(' ')
          print('Invalid Operation: Please try again.')
          time.sleep(1)
          continue

  except ValueError:
    if w == 'esc':
      break

    else:
      print(' ')
      time.sleep(.5)
      print('Invalid Input: Please Try Again')
      continue