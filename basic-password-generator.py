import random,os,time
lent = [] 
with open('sowpods.txt') as f:
    words = f.readlines()
with open('numbers.txt') as f:
    numbers = f.readlines()
with open('symbols.txt') as f:
    symbols = f.readlines()
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
while True:
  x = input('Press Enter to generate a password: ')
  if len(x) == 0:
    for x in range(1,40):
      lent.clear()
      clear()
      randNum1index = random.randint(0, len(numbers) - 1)
      randNum1 = numbers[randNum1index].strip()
      lent.append(randNum1)
      randNum2index = random.randint(0, len(numbers) - 1)
      randNum2 = numbers[randNum2index].strip()
      lent.append(randNum2)
      randWordindex = random.randint(0, len(words) - 1)
      randWord = words[randWordindex].strip()
      lent.append(randWord)
      randSymbol1index = random.randint(0, len(symbols) - 1)
      randSymbol1 = symbols[randSymbol1index].strip()
      lent.append(randSymbol1)
      randSymbol2index = random.randint(0, len(symbols) - 1)
      randSymbol2 = symbols[randSymbol2index].strip()
      lent.append(randSymbol2)
      randSymbol3index = random.randint(0, len(symbols) - 1)
      randSymbol3 = symbols[randSymbol3index].strip()
      lent.append(randSymbol3)
      randSymbol4index = random.randint(0, len(symbols) - 1)
      randSymbol4 = symbols[randSymbol4index].strip()
      lent.append(randSymbol4)
      random.shuffle(lent)
      print('Randomizing: ',*lent,sep='')
      time.sleep(0.05) 
    clear()
    print('Randomized Password: ',*lent,sep='')
    print('\n')
  else:
    print('tryagain')
    continue
  lent.clear()