#using standard function
def compute_pay(hours,rate):
  if hours <= 40:
    ans = rate*hours
  elif hours > 40:
    rate2 = rate*1.5
    hours2 = hours-40
    ans2 = rate*40
    ans = rate2*hours2
    ans = ans+ans2
  return(ans)
hours = input('Enter hours: ')
rate = input('Enter rate: ')
hours = int(hours)
rate = int(rate)
ans = compute_pay(hours,rate)
print(ans)

#using classes badly
class pay:
  def __init__(self,hours,rate,ans):
    self.hours = hours
    self.hours2 = hours-40
    self.rate = rate
    self.rate2 = rate*1.5
    self.ans = ans
  def compute_pay(self):
    if self.hours2 <= 0:
      self.ans = abs(self.hours)*self.rate
      print(self.ans)
    elif self.hours2 > 0:
      self.ans = 40*self.rate
      x = self.hours2*self.rate2
      ans = self.ans+x
      print(ans)

p1 = pay(int(input('Hours: ')),int(input('Rate: ')),0)
p1.compute_pay()