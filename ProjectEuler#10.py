from math import sqrt
import time
init = time.time()
primes = [2]
total = 2
for i in range(3,2000000,2):
    for x in primes:
        if i % x == 0:
            break
        elif x > sqrt(i):
            primes.append(i)
            total += i
            break
    else:
        primes.append(i)
        total += i
print(total)
print("time taken =",time.time()-init)
