jon = input()
doctor = input()

jonrem = jon.partition("h")[0]
doctorrem = doctor.partition("h")[0]

if jonrem.count('a') >= doctorrem.count('a'):
  print('go')
else: print ('no')
