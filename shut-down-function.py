def shut_down(s):
  if s == 'yes':
    return('Shutting down')
  elif s == 'no':
    return('Shutdown Aborted')
  else:
    return('Sorry')
s = input('Confirm shutdown?: ')
s = shut_down(s)
print(s)