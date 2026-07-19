import time as tm
import random as rn
#Hello, world('print')
q = int(input(f'1-10\n'))
for i in range(rn.randint(1, 5) * q):
  print('Hello, world')
  tm.sleep(0.1)
tm.sleep(1)
w = input(f'input\n')
e = tm.time()
while rn.random() < 0.9 and tm.time() - e < 3:
  print(w)
  tm.sleep(0.2)
if tm.time() - e >= 3:
  print('Good luck')
