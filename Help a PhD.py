times = input()
add = ['']*int(times)

for i in range(int(times)):
  add[i] = input()
  
for i in range(int(times)):
  if (add[i] == "P=NP"):
      print('skipped')
  else: 
      split = add[i].split('+')
      print(str(int(split[0]) + int(split[1])))
