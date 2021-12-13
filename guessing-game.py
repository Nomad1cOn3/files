import time
import random

loop1 = '0'
loop2 = '0'
range1 = range(0,101)
randomNumber = '0'
number = '0'
attempts = 1
tryagain = '0'
winner = False

while loop1 == '0':
  randomNumber = random.randrange(0,101)
  while loop2 == '0':
    try:
      print(' ')
      number = input('Guess a number: ')
      number = int(number)
      if number in range(0,101):
        if number == randomNumber:
          winner = True
          break
        elif number > randomNumber:
          print(' ')
          print('Number is too high: Guess again')
          attempts = attempts+1
          continue
        elif number < randomNumber:
          print(' ')
          print('Number is too low: Guess again')
          attempts = attempts+1
          continue
      else:
        raise Exception

    except Exception:
        print(' ')
        print('Guess must be a number in range 0-100: Please Try Again')
        attempts = attempts+1
        continue
      
  if winner == True:
    print('You won!')
    if attempts == 1:
      print(' ')
      print('You guessed the number in',attempts,'attempt')
      print(' ')
      print('Cheater!')
    elif attempts in range(2,10):
      print(' ')
      print('You guessed the number in',attempts,'attempts')
      print(' ')
    else:
      print(' ')
      print('You guessed the number in',attempts,'attempts, stupid. Do better next time Mr. 2 braincells')
    print(' ')
    print(' ')
    time.sleep(1)
    tryagain = input('Would you like to play again? (y/n): ')
    if tryagain == 'y':
      continue
    elif tryagain == 'n':
      break
    else:
      print(' ')
      print("You're dumb :)")
      time.sleep(.5)
      print(' ')
      print('Now play again lol')
      continue