import random as r
import math as m
import time
import multiprocessing as mp

pool = mp.Pool(processes = 4)

start_time = time.time()
# Number of darts that land inside.
inside = 0
# Total number of darts to throw.
total = 10000000
counter = []


def rand_Point():
  global inside
  # Generate random x, y in [0, 1].
  x2 = r.random()**2
  y2 = r.random()**2
  # Increment if inside unit circle.
  if m.sqrt(x2 + y2) < 1.0:
    return 1
  else:
    return 0 

def getResults(res):
    global counter
    counter.append(res)
    if (res == 1):
        counter.append(1)

results = [pool.apply_async(rand_Point, args = ()) for x in range(1, total)]


output = [p.get() for p in results]

pool.close()
pool.join()

# It works!
# inside / total = pi / 4
pi = (float(len(output)) / total) * 4
print(pi)
print("--- %s seconds ---" % (time.time() - start_time))
