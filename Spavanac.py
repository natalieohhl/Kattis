time = input()
time = time.split(" ")

time[1] = int(time[1])-45

if (time[1] < 0): 
  time[0]= int(time[0]) - 1 
  time[1]=60 + time[1]

if (int(time[0]) < 0):
  time[0]= 23

print(str(time[0])+ " " + str(time[1]))
