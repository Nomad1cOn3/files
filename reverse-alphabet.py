import string #imports string module
index = -1 #controls item index
l = list(string.ascii_lowercase) #generates a list of letters - lowercase
l2 = list(string.ascii_uppercase) # generates a list of letters - uppercase
for item in l or l2:
  print(l2[index],l[index])
  index = index-1