chorusi = 1
def chorus(chorusi):
  print('Out of the dark into the light')
  print('Into a new horizon')
  if chorusi == 1:
    print('On your way to the other side')
    print("I know your soul is risin'")
  elif chorusi == 2:
    print("Now that you're on the other side")
    print("A midnight sun is risin'")
  print("And now you're para-paragliding, gliding")
  print("Oh, what a sky to dive in, dive in")
  print("Now you're para-paragliding, gliding")
  print('I see a silver lining')
def bridge():
  print('Carry me, carry me, carry me in your arms')
  print('Carry me, carry me, carry me in your arms')
  print('Oh, cover me, cover me, cover me with your wings')
def outro():
  print('Carry me, carry me, carry me in your arms')
def print_lyrics():
  print('I, I can hear you sigh, why is this goodbye?')
  print("The colour's fading out")
  print('No, no more tears to cry in your diamond eyes')
  print("The battle's over now")
  print('Floating like a ribbon to a new beginning')
  print('Waiting in the afterglow')
  print("Go on your expedition, find what you've been missing")
  print('Go')
  print(' ')
  chorus(1)
  print(' ')
  print('Fly like a firefly with all the stars aligned')
  print('Soaring above the clouds')
  print("No, there's no space and time where night and day collide")
  print("You're off to higher grounds")
  print('To your destination, yeah, the safest haven')
  print('Waiting in the afterglow')
  print("Go on your expedition, find what you've been missing")
  print('Go')
  print(' ')
  chorus(1)
  print(' ')
  bridge()
  print(' ')
  chorus(2)
  print(' ')
  outro()
while True:
  print_lyrics()
  l = input()
  if len(l) == 0:
    break
  else:
    break