total = 0
qty = input()
getinput = input()

expenses = []*int(qty)
expenses = getinput.split()

for i in range(int(qty)):
  if int(expenses[i]) < 0:
    total = total + int(expenses[i])

print(-total)
