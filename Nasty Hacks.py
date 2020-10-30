size = input()
list = ['']*int(size)

for i in range(int(size)) :
  list[i] = input()

for i in range(int(size)) :
  cost = list[i].split(' ')

  if ((int(cost[0]) + int(cost[2]) < int(cost[1]))):
    print('advertise')
  elif ((int(cost[0]) + int(cost[2])) == int(cost[1])):
    print('does not matter')
  else: 
    print ('do not advertise')  
