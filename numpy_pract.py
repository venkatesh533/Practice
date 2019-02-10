
import numpy as np
import time
import sys

size = 1000
l1 = list(range(size))
l2 = list(range(size))

a1 = np.arange(size)
a2 = np.arange(size)

start = time.time()
res = [x+y for x,y in zip(l1,l2)]
print((time.time()-start)*1000)
start = time.time()
res = a1+a2
print((time.time()-start)*1000)