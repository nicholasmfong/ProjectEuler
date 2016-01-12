from math import sqrt
import time
init = time.time()
primes = [2]
for i in range(3,1000000,2):
    for x in primes:
        if i % x == 0:
            break
        elif x > sqrt(i):
            primes.append(i)
            break

longest = 2
terms = 1
for j in range(len(primes)):
    if primes[j] > 50000:
        print("answer =",longest,"terms =",terms)
        break
    total = primes[j]
    n = 1
    while total < 1000000:
        total += primes[j+n]
        n += 1
    if n < terms:
        print("answer =",longest,"terms =",terms)
        break
    while total not in primes and n > 0:
        n -= 1
        total -= primes[j+n]
    if n > 0:
        if n+1 > terms:
            terms = n+1
            longest = total

print("time taken =",time.time()-init)
