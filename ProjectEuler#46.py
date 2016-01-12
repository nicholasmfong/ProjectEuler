import time
init = time.time()
from math import sqrt
primes = [2]
composites = []
for i in range(3,10000,2):
    for x in primes:
        if i % x == 0:
            composites.append(i)
            break
        elif x > sqrt(i):
            primes.append(i)
            break
    else:
        primes.append(i)

for j in composites:
    conjecture = False
    k = 0
    while primes[k] < j:
        l = 1
        while (primes[k] + 2 * (l**2)) < j:
            l += 1
        if(primes[k] + 2 * (l**2)) == j:
            conjecture = True
            break
        else:
            k += 1
    if conjecture == False:
        print(j)
        break
print("it took",time.time()-init,"seconds to run")
