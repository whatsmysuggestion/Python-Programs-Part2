import random as rand
a = 100000
b = 1000000
print('print numbers [', a, ', ', b, '] :', rand.randint(a,b))

start = 1
stop = 12
step = 2 #1 3 5 7 9 11
print('print one number from the sequence :',
      rand.randrange(start, stop, step))