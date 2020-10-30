inputsum = int(input())

if ((inputsum > 0) and (inputsum<=10)):
  if inputsum%4 ==0:
    print('Even')
  elif (inputsum%4 ==2):
    print('Odd')
  else: print('Either')
