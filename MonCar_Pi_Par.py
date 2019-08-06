import random as r
import math as m
import time
import multiprocessing as mp

start_time = time.time()
# Number of darts that land inside.
inside = 0
# Total number of darts to throw.
total = 10000000
counter = mp.Queue()


def rand_Point(counter):
  global inside
  # Generate random x, y in [0, 1].
  x2 = r.random()**2
  y2 = r.random()**2
  # Increment if inside unit circle.
  if m.sqrt(x2 + y2) < 1.0:
    counter.put(0)


processes = [mp.Process(target=rand_Point, args=(counter)) for x in range(total)]

# Run processes
for p in processes:
  p.start()

# Exit completed processes
for p in processes:
  p.join()

output = [counter.get() for p in processes]

# inside / total = pi / 4
pi = (float(len(output)) / total) * 4

# It works!
print(pi)
print("--- %s seconds ---" % (time.time() - start_time))
