import time as tm
import random as rn
#Hello, world('print')
q = int(input(f'1-10\n'))
for i in range(rn.randint(1, 5) * q):
  print('Hello, world')
  tm.sleep(0.1)
