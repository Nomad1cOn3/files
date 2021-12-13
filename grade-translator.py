import time

print('Hello There!')
print(' ')
time.sleep(.5)
print('Welcome to the Numerical-Letter Grade Translator!')

i = '0'
i2 = '0'
tupleaplus = (100,99,98,97)
tuplea = (96,95,94,93)
tupleaminus = (90,91,92)
tuplebplus = (89,88,87)
tupleb = (86,85,84,83)
tuplebminus = (82,81,80)
tuplecplus = (79,78,77)
tuplec = (76,75,74,73)
tuplecminus = (72,71,70)
tupledplus = (69,68,67)
tupled = (66,65)
tuplef = (64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0)
tupleaplus2 = ('A+','a+')
tuplea2 = ('A','a')
tupleaminus2 = ('A-','a-')
tuplebplus2 = ('B+','b+')
tupleb2 = ('B','b')
tuplebminus2 = ('B-','b-')
tuplecplus2 = ('C+','c+')
tuplec2 = ('C','c')
tuplecminus2 = ('C-','c-')
tupledplus2 = ('D+','d+')
tupled2 = ('D','d')
tuplef2 = ('F','f')



while i2 == 'y' or '0':
  if i == 'n':
    break

  else:
    try: 
      while i == 'y' or '0':
        print(' ')
        time.sleep(.5)
        gradein = input("Enter A Grade: ")
        gradein = int(gradein)
        if gradein in tupleaplus:
          print(' ')
          time.sleep(.5)
          print('Grade is an A+')
          print(' ')
          time.sleep(1)
          i = input('Do you want to translate another grade?(y/n): ')
          if i == 'y':
            continue
          if i == 'n':
            break
    
        elif gradein in tuplea:
          print(' ')
          time.sleep(.5)
          print('Grade is an A')
          print(' ')
          time.sleep(1)
          i = input('Do you want to translate another grade?(y/n): ')
          if i == 'y':
            continue
          if i == 'n':
            break

        elif gradein in tupleaminus:
          print(' ')
          time.sleep(.5)
          print('Grade is an A-')
          print(' ')
          time.sleep(1)
          i = input('Do you want to translate another grade?(y/n): ')
          if i == 'y':
            continue
          if i == 'n':
            break

        elif gradein in tuplebplus:
          print(' ')
          time.sleep(.5)
          print('Grade is a B+')
          print(' ')
          time.sleep(1)
          i = input('Do you want to translate another grade?(y/n): ')
          if i == 'y':
            continue
          if i == 'n':
            break

        elif gradein in tupleb:
          print(' ')
          time.sleep(.5)
          print('Grade is a B')
          print(' ')
          time.sleep(1)
          i = input('Do you want to translate another grade?(y/n): ')
          if i == 'y':
            continue
          if i == 'n':
            break

        elif gradein in tuplebminus:
          print(' ')
          time.sleep(.5)
          print('Grade is a B-')
          print(' ')
          time.sleep(1)
          i = input('Do you want to translate another grade?(y/n): ')
          if i == 'y':
            continue
          if i == 'n':
            break

        elif gradein in tuplecplus:
          print(' ')
          time.sleep(.5)
          print('Grade is a C+')
          print(' ')
          time.sleep(1)
          i = input('Do you want to translate another grade?(y/n): ')
          if i == 'y':
            continue
          if i == 'n':
            break

        elif gradein in tuplec:
          print(' ')
          time.sleep(.5)
          print('Grade is a C')
          print(' ')
          time.sleep(1)
          i = input('Do you want to translate another grade?(y/n): ')
          if i == 'y':
            continue
          if i == 'n':
            break

        elif gradein in tuplecminus:
          print(' ')
          time.sleep(.5)
          print('Grade is a C-')
          print(' ')
          time.sleep(1)
          i = input('Do you want to translate another grade?(y/n): ')
          if i == 'y':
            continue
          if i == 'n':
            break

        elif gradein in tupledplus:
          print(' ')
          time.sleep(.5)
          print('Grade is a D+')
          print(' ')
          time.sleep(1)
          i = input('Do you want to translate another grade?(y/n): ')
          if i == 'y':
            continue
          if i == 'n':
            break

        elif gradein in tupled:
          print(' ')
          time.sleep(.5)
          print('Grade is a D')
          print(' ')
          time.sleep(1)
          i = input('Do you want to translate another grade?(y/n): ')
          if i == 'y':
            continue
          if i == 'n':
            break

        elif gradein in tuplef:
          print(' ')
          time.sleep(.5)
          print('Grade is an F')
          print(' ')
          time.sleep(1)
          i = input('Do you want to translate another grade?(y/n): ')
          if i == 'y':
            continue
          if i == 'n':
            break

        else:
          print(' ')
          time.sleep(1)
          print('Value Not Recognized: Please Try Again')
          continue

    except ValueError:
      if gradein in tupleaplus2:
        print(' ')
        time.sleep(.5)
        print('Grade could be in range:',tupleaplus)
        print(' ')
        time.sleep(1)
        i = input('Do you want to translate another grade?(y/n): ')
        if i == 'y':
          continue
        if i == 'n':
          break

      elif gradein in tuplea2:
        print(' ')
        time.sleep(.5)
        print('Grade could be in range:',tuplea)
        print(' ')
        time.sleep(1)
        i = input('Do you want to translate another grade?(y/n): ')
        if i == 'y':
          continue
        if i == 'n':
          break

      elif gradein in tupleaminus2:
        print(' ')
        time.sleep(.5)
        print('Grade could be in range:',tupleaminus)
        print(' ')
        time.sleep(1)
        i = input('Do you want to translate another grade?(y/n): ')
        if i == 'y':
          continue
        if i == 'n':
          break

      elif gradein in tuplebplus2:
        print(' ')
        time.sleep(.5)
        print('Grade could be in range:',tuplebplus)
        print(' ')
        time.sleep(1)
        i = input('Do you want to translate another grade?(y/n): ')
        if i == 'y':
          continue
        if i == 'n':
          break

      elif gradein in tupleb2:
        print(' ')
        time.sleep(.5)
        print('Grade could be in range:',tupleb)
        print(' ')
        time.sleep(1)
        i = input('Do you want to translate another grade?(y/n): ')
        if i == 'y':
          continue
        if i == 'n':
          break

      elif gradein in tuplebminus2:
        print(' ')
        time.sleep(.5)
        print('Grade could be in range:',tuplebminus)
        print(' ')
        time.sleep(1)
        i = input('Do you want to translate another grade?(y/n): ')
        if i == 'y':
          continue
        if i == 'n':
          break

      elif gradein in tuplecplus2:
        print(' ')
        time.sleep(.5)
        print('Grade could be in range:',tuplecplus)
        print(' ')
        time.sleep(1)
        i = input('Do you want to translate another grade?(y/n): ')
        if i == 'y':
          continue
        if i == 'n':
          break

      elif gradein in tuplec2:
        print(' ')
        time.sleep(.5)
        print('Grade could be in range:',tuplec)
        print(' ')
        time.sleep(1)
        i = input('Do you want to translate another grade?(y/n): ')
        if i == 'y':
          continue
        if i == 'n':
          break

      elif gradein in tuplecminus2:
        print(' ')
        time.sleep(.5)
        print('Grade could be in range:',tuplecminus)
        print(' ')
        time.sleep(1)
        i = input('Do you want to translate another grade?(y/n): ')
        if i == 'y':
          continue
        if i == 'n':
          break

      elif gradein in tupledplus2:
        print(' ')
        time.sleep(.5)
        print('Grade could be in range:',tupledplus)
        print(' ')
        time.sleep(1)
        i = input('Do you want to translate another grade?(y/n): ')
        if i == 'y':
          continue
        if i == 'n':
          break

      elif gradein in tupled2:
        print(' ')
        time.sleep(.5)
        print('Grade could be in range:',tupled)
        print(' ')
        time.sleep(1)
        i = input('Do you want to translate another grade?(y/n): ')
        if i == 'y':
          continue
        if i == 'n':
          break

      elif gradein in tuplef2:
        print(' ')
        time.sleep(.5)
        print('Grade could be in range:',tuplef)
        print(' ')
        time.sleep(1)
        i = input('Do you want to translate another grade?(y/n): ')
        if i == 'y':
          continue
        if i == 'n':
          break

      else:
        print(' ')
        time.sleep(1)
        print('Value Not Recognized: Please Try Again')
        continue