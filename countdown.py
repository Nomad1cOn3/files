import time
time_var = int(input('How many seconds would you like to set a timer for?: '))
for x in reversed(range(time_var+1)):
    print(f'Time remaining: {x} seconds')
    time.sleep(1)
print('Timer Done!')