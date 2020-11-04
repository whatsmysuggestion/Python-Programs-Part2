import random as rand
string = "kkar technologies"
li = [11, 12, 13, 14, 101, 151]
print('Single character:',rand.choice(string))
print('random number :', rand.choice(li))
print('random string of length 4 chars:',rand.sample(string, 4))
print('random string of length 4 values :',rand.sample(li, 4))
rand.shuffle(li)
print('shuffled list values:', li)