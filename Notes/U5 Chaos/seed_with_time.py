from time import time
from random import randint, seed

now = time()
print(now)

seed(now)
print(randint(0, 100))
